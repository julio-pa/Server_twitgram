from django.db import models
from django.utils import timezone
from apps.user.models import UserAccount
# from cloudinary.models import CloudinaryField


# def blog_thumbnail_directory(filename):
#     return cloudinary.uploader.upload(f'{filename}',
#                                       public_id=f'{filename}')

# def cloudinary_upload(filename):
#     cloudinary.uploader.upload(request.FILES[f'{filename}'])


# Create your models here.


class Tweet(models.Model):

    # class TweetObjects(models.Manager):
    #     # def get_queryset(self):
    #     #     return super().get_queryset().filter(status='published')
    # id = models.CharField(primary_key=True, editable=False, max_length=10)
    user = models.ForeignKey(
        UserAccount, related_name='user', on_delete=models.PROTECT, null=True)
    thumbnail = models.ImageField(
        upload_to='images/', max_length=5000, blank=True, null=True)

    description = models.TextField(max_length=400)

    published = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0, blank=True)

    objects = models.Manager()  # default manager
    # postobjects = TweetObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.description

    # def get_view_count(self):
    #     likes = ViewCount.objects.filter(tweet=self).count()
    #     return likes

    # def save(self, **kwargs):
    #     if not self.id:

    #         self.id = uuid.uuid4()

    #     super().save(*kwargs)


class ViewCount(models.Model):
    tweet = models.ForeignKey(
        Tweet, related_name='tweet_view_count', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address}"
