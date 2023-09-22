from django.shortcuts import render

from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks
from .models import Photo
from .forms import PhotoForm
from .serializers import ImageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


def upload(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)


class GetImagesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Photo.objects.all().exists():

            Images = Photo.objects.all()

            serializer = ImageSerializer(Images, many=True)

            return Response({'images': serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class IndividualImagesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if Photo.objects.filter(id=id).exists():

            img = Photo.objects.get(id=id)
            serializer = ImageSerializer(img)

            return Response({'images': serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
