from django.db import models
from django.utils import timezone
from apps.user.models import User


def blog_thumbnail_directory(instance, filename):
    return 'tweet/{0}/{1}'.format(instance.id, filename)


# Create your models here.


class Tweet(models.Model):

    # class TweetObjects(models.Manager):
    #     # def get_queryset(self):
    #     #     return super().get_queryset().filter(status='published')

    user = models.ForeignKey(
        User, related_name='user_name', on_delete=models.CASCADE)
    thumbnail = models.ImageField(
        upload_to=blog_thumbnail_directory, max_length=500)

    description = models.TextField(max_length=400)

    published = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0, blank=True)

    objects = models.Manager()  # default manager
    # postobjects = TweetObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.description

    def get_view_count(self):
        likes = ViewCount.objects.filter(tweet=self).count()
        return likes


class ViewCount(models.Model):
    tweet = models.ForeignKey(
        Tweet, related_name='tweet_view_count', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address}"
