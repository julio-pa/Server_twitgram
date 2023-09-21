from django.urls import path

from .views import *

urlpatterns = [
    path('images', GetImagesView.as_view()),
]
