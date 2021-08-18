from rest_framework import serializers
from src.profiles.serializers import SocUserByFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):
    followers = SocUserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('followers',)
