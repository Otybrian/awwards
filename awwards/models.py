from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=100)
    location = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True, max_length=100)
    profile_pic = models.ImageField(upload_to='images/')
    bio = models.TextField(blank=True, max_length=1000)
