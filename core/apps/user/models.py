from django.db import models

from django.utils import timezone
# import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


# @receiver(pre_save, sender=UserAccount)
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    # id = models.CharField(primary_key=True, editable=False, max_length=10)
    username = models.CharField(max_length=64)
    email = models.EmailField(
        max_length=255, unique=True)
    img_perfil = models.ImageField(blank=True, null=True)
    banner = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=70, blank=True, default='no bio yet')
    joined = models.DateTimeField(default=timezone.now)
    following = models.IntegerField(default=0, blank=True)
    followers = models.IntegerField(default=0, blank=True)
    is_staff = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=True)

    objects = UserAccountManager()

    class Meta:
        ordering = ('-joined', )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
