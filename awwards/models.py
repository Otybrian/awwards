from django.db import models
import datetime as dt
from django.contrib.auth.models import User
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


class Project(models.Model):
    title = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    description = models.TextField(max_length=255)
    link = models.URLField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project")
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.title

    def delete_post(self):
        self.delete()
    
    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()


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
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    design =  models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    des_likes = models.PositiveIntegerField(default=0)
    des_unlikes = models.PositiveIntegerField(default=0)
    average_design = models.FloatField(default=0, blank=True)
    usability =  models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    use_likes = models.PositiveIntegerField(default=0)
    use_unlikes = models.PositiveIntegerField(default=0)
    average_usability = models.FloatField(default=0, blank=True)
    content =  models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    cont_likes = models.PositiveIntegerField(default=0)
    cont_unlikes = models.PositiveIntegerField(default=0)
    average_content = models.FloatField(default=0, blank=True)
    score = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'

