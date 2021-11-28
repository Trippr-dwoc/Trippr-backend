from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    username = models.CharField(max_length = 30, blank = False, null = False,unique= True)
    first_name = models.CharField(max_length = 30, blank = False, null = False)
    last_name = models.CharField(max_length = 150, blank = False, null = False)
    email = models.EmailField(('email address'), unique=True)
    phone = models.CharField(max_length = 20, blank = False, unique = True, null = False)
    relations = models.ManyToManyField("self", through='Relation');

class Relation(models.Model):
    user_1 = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_1')
    user_2 = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    relation = models.CharField(max_length=1, choices=(
        ('F','Friend'),
        ('B','Block')
    ))

    def __str__(self): 
        return self.user_1.username + ' ' + self.relation + ' ' + self.user_2.username 
