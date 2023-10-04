from PIL import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .pagination import SmallSetPagination
from .permissions import IsPostAuthorOrReadOnly, AuthorPermission

from .models import Tweet
from .serializers import TweetSerializer

from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser


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
    # permission_classes = (AuthorPermission,)
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)
    # serializer_class = PostSerializer

    def post(self, request, format=None):
        # print(request.data)
        tweet_serializer = TweetSerializer(data=request.data)
        # print(tweet_serializer)
        if tweet_serializer.is_valid():
            tweet_serializer.save()
            return Response(tweet_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(tweet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
