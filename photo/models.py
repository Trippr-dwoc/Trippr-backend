from django.db import models
from trip.models import Trip
from user.models import UserProfile

# Create your models here.
class Photo(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete = models.CASCADE)
    location = models.FileField(upload_to='uploads/%Y/%m/%d/')
    users = models.ManyToManyField(UserProfile)

    def __str__(self):
        return (str(self.location.name))