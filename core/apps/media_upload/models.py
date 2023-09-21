from django.db import models
from django.db.models import Max
import uuid
# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=10)
    image = CloudinaryField('image')

    def __str__(self):
        return str(self.image)

    def save(self, **kwargs):
        if not self.id:

            self.id = uuid.uuid4()

        super().save(*kwargs)
