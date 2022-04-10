from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=100,null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
    

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField("image")
    description = models.TextField()
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images    

    def str(self):
        return self.user.username


RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    average = models.IntegerField(default=0, blank=True, null=True)

    def str(self):
        return self.user.username

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'

class Review(models.Model):
    review = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)



