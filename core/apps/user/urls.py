from django.urls import path

from .views import *

urlpatterns = [
    path('users', UserListView.as_view()),
    path('profile/<username>', UserPerfil.as_view()),
    path('update', UpdateProfile.as_view())
]
