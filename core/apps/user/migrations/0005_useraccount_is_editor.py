# Generated by Django 4.2.5 on 2023-09-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_useraccount_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_editor',
            field=models.BooleanField(default=True),
        ),
    ]
