# Generated by Django 4.2.5 on 2023-09-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_alter_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
