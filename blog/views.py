from django.views import generic, View
from django.shortcuts import render, get_object_or_404

from .models import Post


class PostList(generic.ListView):
    """List view to display posts on home page"""

    context_object_name = "posts"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 2


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
