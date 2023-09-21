from django.urls import path

from .views import *

urlpatterns = [
    path('list', TweetListView.as_view()),
    path('create', CreateTweetView.as_view())
]
