from rest_framework import serializers
from .models import SocUser


class GetSocUserSerializer(serializers.ModelSerializer):
    # Получение информации о пользователе
    class Meta:
        model = SocUser
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetSocUserPublicSerializer(serializers.ModelSerializer):
    # Получение публичной информации о пользователе
    class Meta:
        model = SocUser
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )
