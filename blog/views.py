from django.views import generic, View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post


class PostList(generic.ListView):
    """List view to display posts on home page"""

    context_object_name = "posts"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"

    # https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html
    def my_pagination(self, request):
        """function that paginates queries. Used only to fix waypoint infinite scrolling"""
        queryset = Post.objects.filter(status=1).order_by("-created_on")
        page_number = request.GET.get("page", 4)
        paginator = Paginator(queryset, 1)

        try:
            queryset = paginator.page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {"page_post": queryset})


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        posted = queryset.latest("created_on")

        context = {
            "post": post,
            "posted": posted,
        }
        return render(request, "blog/post_detail.html", context)


class AddPost(generic.CreateView):
    model = Post
    template_name = "blog/add_post.html"
    fields = (
        "title",
        "slug",
        "author",
        "featured_image",
        "category",
        "content",
        "status",
    )


class EditPost(generic.UpdateView):
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


class DeletePost(generic.DeleteView):
    model = Post
    template_name = "blog/includes/delete_post.html"
    success_url = reverse_lazy("home")
