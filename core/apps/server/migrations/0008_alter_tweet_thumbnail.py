# Generated by Django 4.2.5 on 2023-10-02 19:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_alter_tweet_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
