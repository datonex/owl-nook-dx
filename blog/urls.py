from django.urls import path
from django.conf.urls import url
from .views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("articles/<slug:slug>", PostDetail.as_view(), name="post_detail"),
]
