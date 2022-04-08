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

    def __str__(self):
        return f' {self.user.username} Profile'


class Projects(models.Model):
    title = models.CharField(max_length=155)
    photo = models.ImageField(manual_crop='1280x720')
    description = models.TextField(max_length=255)
    link = models.URLField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.title

    def delete_post(self):
        self.delete()
