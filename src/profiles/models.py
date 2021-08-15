from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

# Create your models here.

class SocUser(AbstractBaseUser):
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)