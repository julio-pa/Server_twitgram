# Generated by Django 4.2.5 on 2023-10-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_alter_tweet_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
