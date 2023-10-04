from django.http.response import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import UserAccount
from .serializers import UserSerializer
from .pagination import SmallSetPagination


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


class UpdateProfile(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UserSerializer

    def put(self, request, format=None):
        # user = self.request.user

        data = self.request.data
        user_id = data['id']

        print(data)

        profile = UserAccount.objects.get(id=user_id)

        if (data['username']):
            if not (data['username'] == 'undefined'):
                profile.username = data['username']
                profile.save()

        if (data['bio']):
            if not (data['bio'] == 'undefined'):
                profile.bio = data['bio']
                profile.save()

        if (data['img_perfil']):
            if not (data['img_perfil'] == 'undefined'):
                profile.img_perfil = data['img_perfil']
                profile.save()
        if (data['banner']):
            if not (data['banner'] == 'undefined'):
                profile.banner = data['banner']
                profile.save()

        return Response({'perfil': 'profile updated'}, status=status.HTTP_200_OK)
