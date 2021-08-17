from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "published", "create_date", "moderation", "view_count", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    mptt_level_indent = 15
