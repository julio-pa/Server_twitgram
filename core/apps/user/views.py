from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import permissions
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination

from .models import UserAccount
from .serializers import UserSerializer
from django.http.response import JsonResponse
# Create your views here.


class UserListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if UserAccount.objects.all().exists():

            users = UserAccount.objects.all()

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(users, request)
            serializer = UserSerializer(results, many=True)

            return paginator.get_paginated_response({'users': serializer.data})
        else:
            return Response({'error': 'No users found'}, status=status.HTTP_404_NOT_FOUND)


class UserPerfil(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, username, format=None):
        if UserAccount.objects.filter(username=username).exists():

            perfil = UserAccount.objects.get(username=username)
            serializer = UserSerializer(perfil)

            return Response({'perfil': serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
