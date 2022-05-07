from django.urls import path
from django.conf.urls import url

from .views import UserDraftPostList, UserPostBookmarkList, PostBookmark

urlpatterns = [
    path("<int:pk>/drafts/", UserDraftPostList.as_view(), name="draft_view"),
    path("<int:pk>/bookmarks/", UserPostBookmarkList.as_view(), name="bookmark_view"),
    path("bookmark/<slug:slug>/", PostBookmark.as_view(), name="post_bookmark"),
]
