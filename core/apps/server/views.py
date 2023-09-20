from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import permissions
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination

from .models import Tweet
from .serializers import TweetSerializer


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


