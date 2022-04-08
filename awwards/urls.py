from django.urls import path
from .import views


urlpatterns=[
    path('', views.home, name = 'home'),
    path('newproject', views.newProject, name = 'add_Project'),
]

