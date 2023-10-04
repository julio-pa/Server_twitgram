from django.contrib import admin

# from .models import *
from . import models


@admin.register(models.UserAccount)
class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username',
                    'email',)
    search_fields = ('id', 'username',
                     'email',)
