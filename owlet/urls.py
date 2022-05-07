from django.urls import path
from django.conf.urls import url

from .views import UserDraftPostList

urlpatterns = [
    path("<int:pk>/drafts/", UserDraftPostList.as_view(), name="draft_view"),
]
