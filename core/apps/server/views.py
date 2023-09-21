from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination
from .permissions import IsPostAuthorOrReadOnly, AuthorPermission

from .models import Tweet
from .serializers import TweetSerializer
from apps.user.models import User

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


class TweetListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Tweet.objects.all().exists():

            tweets = Tweet.objects.all()

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(tweets, request)
            serializer = TweetSerializer(results, many=True)

            return paginator.get_paginated_response({'posts': serializer.data})
        else:
            return Response({'error': 'No posts found'}, status=status.HTTP_404_NOT_FOUND)


class CreateTweetView(APIView):
    permission_classes = (AuthorPermission,)

    def post(self, request, format=None):
        tweet_data = JSONParser().parse(request)
        tweet_serializer = TweetSerializer(data=tweet_data)

        if tweet_serializer.is_valid():
            tweet_serializer.save()
            return Response({'succes:tweet created'}, status=status.HTTP_200_OK)

        return JsonResponse(tweet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
