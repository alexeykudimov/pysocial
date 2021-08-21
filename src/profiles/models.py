from django.contrib.auth.models import AbstractUser
from django.db import models


class SocUser(AbstractUser):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    first_login = models.DateTimeField(blank=True, null=True, verbose_name='Дата первого входа')
    phone = models.CharField(max_length=14, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True, verbose_name='Аватар')
    bio = models.TextField(blank=True, null=True, verbose_name='Биография')
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=6, choices=GENDER, default='male', verbose_name='Пол')
    technology = models.ManyToManyField('Technology', related_name='users', verbose_name='Технологии')

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'


class Technology(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'технологию'
        verbose_name_plural = 'технологии'
