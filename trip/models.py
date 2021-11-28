from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import deactivate

from user.models import UserProfile
# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100, null=False)
    status = CharField(max_length=1, null=False, choices=(
        ('A','Active'),
        ('O','Over')
    ))
    users = ManyToManyField(UserProfile)

    def __str__(self): 
        return self.name

