from django.db import models
from django.conf import settings


class Follower(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner', verbose_name='Пользователь'
    )
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers', verbose_name='Подписчик'
    )

    def __str__(self):
        return f"Relation #{self.id}"

    class Meta:
        verbose_name = 'подписчика'
        verbose_name_plural = 'подписчики'