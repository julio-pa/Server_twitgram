from rest_framework import serializers

from .models import *


class TweetSerializer(serializers.ModelSerializer):

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
