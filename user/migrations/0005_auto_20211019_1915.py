# Generated by Django 3.2.3 on 2021-10-19 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_relations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='relations',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='x',
            field=models.ManyToManyField(related_name='_user_userprofile_x_+', through='user.Relation', to=settings.AUTH_USER_MODEL),
        ),
    ]
