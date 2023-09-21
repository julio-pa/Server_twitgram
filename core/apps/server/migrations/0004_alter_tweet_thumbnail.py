# Generated by Django 4.2.5 on 2023-09-21 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_upload', '0001_initial'),
        ('server', '0003_alter_tweet_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='img_url', to='media_upload.photo'),
        ),
    ]
