from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    image = CloudinaryField('image')

    def __str__(self):
        return str(self.image)
