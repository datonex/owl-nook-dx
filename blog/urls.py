from django.urls import path
from django.conf.urls import url
from .views import DeletePost, PostList, PostDetail, AddPost, EditPost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("articles/<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("articles/add_post/", AddPost.as_view(), name="add_post"),
    path("articles/edit/<int:pk>", EditPost.as_view(), name="edit_post"),
    path("articles/delete/<int:pk>", DeletePost.as_view(), name="delete_post"),
]
