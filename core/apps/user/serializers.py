from rest_framework import serializers
from .models import *
# Djoser
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        ordering = ('-published',)
        fields = [
            'id',
            'username',
            'email',
            'img_perfil',
            'banner',
            'bio',
            'joined',
            'following',
            'followers',
        ]
