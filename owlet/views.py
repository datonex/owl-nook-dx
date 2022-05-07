from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from blog.models import Post


class UserDraftPostList(LoginRequiredMixin, generic.ListView):
    """List view to display drafts for current user"""

    template_name = "owlet/drafts.html"

    def get(self, request, pk):
        if request.user.id == pk:
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

            context = {
                "drafts": drafts,
                "page_post": queryset,
            }

            return render(request, self.template_name, context)
        else:
            messages.error(request, "This is not your account")
            return HttpResponseRedirect("/")


class PostBookmark(LoginRequiredMixin, View):
    """Handler to add/remove user if post is bookmarked"""

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        username = request.user
        if post.bookmark.filter(pk=username.id).exists():
            post.bookmark.remove(username)
        else:
            post.bookmark.add(username)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class UserPostBookmarkList(LoginRequiredMixin, generic.ListView):
    """Display the users bookmarks"""

    template_name = "owlet/bookmarks.html"

    def get(self, request, pk):
        if request.user.id == pk:
            bookmarks = Post.objects.filter(status=1, bookmark=pk)

            queryset = bookmarks
            page_number = request.GET.get("page", 1)
            paginator = Paginator(queryset, 10)

            try:
                queryset = paginator.page(page_number)
            except PageNotAnInteger:
                queryset = paginator.page(1)
            except EmptyPage:
                queryset = paginator.page(paginator.num_pages)

            context = {
                "bookmarks": bookmarks,
                "page_post": queryset,
            }
            return render(request, self.template_name, context)
        else:
            messages.error(request, "This is not your account")
            return HttpResponseRedirect("/")
