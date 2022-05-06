from django.urls import path
from django.conf.urls import url
from .views import (
    AddCategory,
    CategoryPostList,
    DeletePost,
    PostLike,
    PostList,
    PostDetail,
    AddPost,
    EditPost,
    UserDraftPostList,
)

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("articles/<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>", PostLike.as_view(), name="post_like"),
    path("articles/add_post/", AddPost.as_view(), name="add_post"),
    path("articles/edit/<int:pk>", EditPost.as_view(), name="edit_post"),
    path("articles/delete/<int:pk>", DeletePost.as_view(), name="delete_post"),
    path("categories/add_category/", AddCategory.as_view(), name="add_category"),
    path(
        "categories/category/<slug:slug>/",
        CategoryPostList.as_view(),
        name="category_view",
    ),
    path("owlet/<int:pk>/drafts/", UserDraftPostList.as_view(), name="draft_view"),
]
