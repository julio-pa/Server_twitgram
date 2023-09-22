from django.urls import path

from .views import *

urlpatterns = [
    path('images', GetImagesView.as_view()),
    path('img_url/<id>', IndividualImagesView.as_view()),
]
