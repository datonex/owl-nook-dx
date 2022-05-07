from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    UserDraftPostList,
    UserEditProfile,
    UserPostBookmarkList,
    PostBookmark,
)

urlpatterns = [
    path("<int:pk>/drafts/", UserDraftPostList.as_view(), name="draft_view"),
    path("<int:pk>/bookmarks/", UserPostBookmarkList.as_view(), name="bookmark_view"),
    path("bookmark/<slug:slug>/", PostBookmark.as_view(), name="post_bookmark"),
    path("<int:pk>/edit_profile/", UserEditProfile.as_view(), name="edit_profile"),
    path(
        "password/",
        auth_views.PasswordChangeView.as_view(template_name="owlet/edit_password.html"),
        name="edit_password",
    ),
]
