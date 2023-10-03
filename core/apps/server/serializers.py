from rest_framework import serializers

from .models import *

from apps.user.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'thumbnail',
            'description',
            'published',
            'likes'
        ]
        # depth = 1

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        instance.save()
        return response

# TODO: Create a new serializer for the post request


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'user',
            'thumbnail',
            'description',
        ]
