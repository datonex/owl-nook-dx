from email import message
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaultfilters import slugify


from .models import Post, Category
from .forms import CommentForm

# https://github.com/skorokithakis/shortuuid
# https://stackoverflow.com/questions/2546575/how-to-update-the-filename-of-a-djangos-filefield-instance
# https://cpadiernos.github.io/function-based-views-and-their-class-based-view-equivalents-in-django-part-one.html


class RedirectToPreviousMixin:
    # https://stackoverflow.com/questions/62626660/redirect-back-to-previous-page-django
    """
    Redirection class to return to page the user came form after form
    submission, if no previous page exists, user will be redirected to
    home page
    """

    default_redirect = "/"

    def get(self, request, *args, **kwargs):
        request.session["previous_page"] = request.META.get(
            "HTTP_REFERER", self.default_redirect
        )
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session["previous_page"]


class PostList(generic.ListView):
    """List view to display posts on home page"""

    context_object_name = "posts"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"

    # https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html
    def my_pagination(self, request):
        """
        function that paginates queries. Used only to fix waypoint
        infinite scrolling bug when class based pagination is used
        """
        queryset = self.queryset
        page_number = request.GET.get("page", 1)
        paginator = Paginator(queryset, 10)

        try:
            queryset = paginator.page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {"page_post": queryset})


class PostDetail(View):
    """Class to return post details, including handling comments, and like/dislikes"""

    template_name = "blog/post_detail.html"

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        posted = queryset.latest("created_on")
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        bookmarked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True

        context = {
            "post": post,
            "posted": posted,
            "liked": liked,
            "bookmarked": bookmarked,
            "comments": comments,
            "comment_form": CommentForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        liked = False
        bookmarked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(request.META["HTTP_REFERER"])
        else:
            comment_form = CommentForm()

        return render(
            request,
            self.template_name,
            {
                "post": post,
                "liked": liked,
                "bookmarked": bookmarked,
                "comments": comments,
                "comment_form": comment_form,
            },
        )


class PostLike(LoginRequiredMixin, View):
    """Handler to add/remove user if post is liked"""

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        username = request.user

        if post.likes.filter(id=username.id).exists():
            post.likes.remove(username)
        else:
            post.likes.add(username)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class AddPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """Class to handle adding a blog post for users"""

    model = Post
    template_name = "blog/add_post.html"
    fields = (
        "title",
        "slug",
        "excerpt",
        "category",
        "featured_image",
        "content",
        "status",
    )
    success_message = "%(title)s was created successfully"

    # https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.POST["status"] == 1:
            return reverse("post_detail", args=[self.request.POST["slug"]])
        else:
            return reverse_lazy("draft_view", args=[self.request.user.id])


class EditPost(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """Class to handle editing a blog post for users"""

    model = Post
    fields = (
        "title",
        "slug",
        "excerpt",
        "featured_image",
        "category",
        "content",
        "status",
    )
    template_name = "blog/edit_post.html"
    success_message = "%(title)s was edited successfully"

    def get_success_url(self):
        if self.request.POST["status"] == 1:
            return reverse("post_detail", args=[self.request.POST["slug"]])
        else:
            return reverse_lazy("draft_view", args=[self.request.user.id])


class DeletePost(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    """Class to handle deleting their blog post for users"""

    model = Post
    template_name = "blog/includes/delete_post.html"
    success_url = reverse_lazy("home")
    success_message = "%(title)s was deleted successfully"


class AddCategory(
    LoginRequiredMixin, RedirectToPreviousMixin, SuccessMessageMixin, generic.CreateView
):
    """Class to handle adding a blog categories for users"""

    model = Category
    template_name = "blog/add_category.html"
    fields = "__all__"

    success_message = "%(name)s was created successfully"
    success_url = reverse_lazy("add_post")


class CategoryPostList(generic.ListView):
    """List view to display posts with specific category"""

    template_name = "blog/category.html"

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        category_posts = Post.objects.filter(status=1, category=category)

        queryset = category_posts
        page_number = request.GET.get("page", 1)
        paginator = Paginator(queryset, 10)

        try:
            queryset = paginator.page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {
            "category": category,
            "category_posts": category_posts,
            "page_post": queryset,
        }

        return render(request, self.template_name, context)


def search(request):
    """search query handler"""

    template = "blog/search.html"
    total_posts = 0
    query = None
    posts = Post.objects.filter(status=1)

    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            messages.error(request, ("You didn't enter any search criteria!"))
            return redirect(reverse("home"))

        queries = (
            Q(title__icontains=query)
            | Q(author__username__icontains=query)
            | Q(category__name__icontains=query)
        )
        posts = posts.filter(queries)
        total_posts = posts.count()

    page_number = request.GET.get("page", 1)
    paginator = Paginator(posts, 60)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "search_query": query,
        "total_posts": total_posts,
        "page_post": posts,
    }

    return render(request, template, context)
