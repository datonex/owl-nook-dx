from django.contrib import admin
from django.db import models
from .models import Post, Category
from tinymce.widgets import TinyMCE


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
    list_display = ("name", "description")
