from django.contrib import admin
from django.db import models
from .models import Post, Category, Comment
from tinymce.widgets import TinyMCE


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinyInject.js",)

    list_display = (
        "author",
        "title",
        "status",
        "created_on",
    )
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {
        "slug": ("title",),
    }
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "description")
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
