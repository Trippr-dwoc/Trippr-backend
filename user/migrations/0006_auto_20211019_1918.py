# Generated by Django 3.2.3 on 2021-10-19 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211019_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='x',
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
