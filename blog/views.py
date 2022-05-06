from django.views import generic, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            "post": post,
            "posted": posted,
            "liked": liked,
            "comments": comments,
            "comment_form": CommentForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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
                "comments": comments,
                "comment_form": comment_form,
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        username = request.user

        if post.likes.filter(id=username.id).exists():
            post.likes.remove(username)
        else:
            post.likes.add(username)

        if post.dislikes.filter(id=username.id).exists():
            post.dislikes.remove(username)
        else:
            post.dislikes.add(username)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class AddPost(LoginRequiredMixin, generic.CreateView):
    """Class to handle adding a blog post for users"""

    model = Post
    template_name = "blog/add_post.html"
    fields = (
        "title",
        "slug",
        "featured_image",
        "category",
        "content",
        "status",
    )

    # https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, generic.UpdateView):
    """Class to handle editing a blog post for users"""

    model = Post
    fields = (
        "title",
        "slug",
        "featured_image",
        "category",
        "content",
        "status",
    )
    template_name = "blog/edit_post.html"

    def get_success_url(self):
        if self.request.POST["status"] == 1:
            return reverse("post_detail", args=[self.request.POST["slug"]])
        else:
            return reverse_lazy("draft_view", args=[self.request.user.id])


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    """Class to handle deleting their blog post for users"""

    model = Post
    template_name = "blog/includes/delete_post.html"
    success_url = reverse_lazy("home")


class AddCategory(LoginRequiredMixin, RedirectToPreviousMixin, generic.CreateView):
    """Class to handle adding a blog categories for users"""

    model = Category
    template_name = "blog/add_category.html"
    fields = "__all__"


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


class UserDraftPostList(generic.ListView):
    """List view to display drafts for current user"""

    template_name = "blog/drafts.html"

    def get(self, request, pk):
        drafts = Post.objects.filter(status=0, author=pk)

        queryset = drafts
        page_number = request.GET.get("page", 1)
        paginator = Paginator(queryset, 10)

        try:
            queryset = paginator.page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        request.session["from_drafts"] = True
        context = {
            "drafts": drafts,
            "page_post": queryset,
        }

        return render(request, self.template_name, context)
