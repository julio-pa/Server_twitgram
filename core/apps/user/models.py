from django.db import models
# from apps.server.models import Tweet
from django.utils import timezone
# Create your models here.


def user_img_directory(instance, filename):
    return 'user/{0}/{1}'.format(instance.name, filename)


class User(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    slug = models.CharField(max_length=255)
    img_perfil = models.ImageField(
        upload_to=user_img_directory, max_length=500)
    banner = models.ImageField(
        upload_to=user_img_directory, max_length=500)
    bio = models.CharField(max_length=70)
    joined = models.DateTimeField(default=timezone.now)
    following = models.IntegerField(default=0, blank=True)
    followers = models.IntegerField(default=0, blank=True)
    # tweets = models.ForeignKey(
    #     Tweet, related_name='user_tweets', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
