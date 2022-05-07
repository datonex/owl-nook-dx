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
