from django.db import models
# from apps.server.models import Tweet
from django.utils import timezone
import uuid
# Create your models here.


# def user_img_directory(instance, filename):
#     return 'user/{0}/{1}'.format(instance.name, filename)


class User(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=10)
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    img_perfil = models.ImageField(default='user-icon.webp', blank=True)
    banner = models.ImageField(default='userbanner.jpg', blank=True)
    bio = models.CharField(max_length=70)
    joined = models.DateTimeField(default=timezone.now)
    following = models.IntegerField(default=0, blank=True)
    followers = models.IntegerField(default=0, blank=True)
    # tweets = models.ForeignKey(
    #     Tweet, related_name='user_tweets', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.id:

            self.id = uuid.uuid4()

        super().save(*kwargs)
