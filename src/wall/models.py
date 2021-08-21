from django.db import models
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from src.comments.models import AbstractComment


class Post(models.Model):

    text = models.TextField(max_length=1000, verbose_name='Текст поста')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    moderation = models.BooleanField(default=True, verbose_name='Прошел модерацию')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', verbose_name='Пользователь'
    )

    def __str__(self):
        return f"Post {self.id}"

    def comments_count(self):
        return self.comments.count()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(AbstractComment, MPTTModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, verbose_name='Пост')
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительский комментарий'
    )

    def __str__(self):
        return f"{self.user} - {self.post}"

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
