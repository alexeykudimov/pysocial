from django.db import models


class AbstractComment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст комментария')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    deleted = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True
