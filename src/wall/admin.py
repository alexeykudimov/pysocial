from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "create_date", "view_count", "published", "moderation",)


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_date", "update_date", "published",)
    mptt_level_indent = 15
