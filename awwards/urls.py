from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name='profile'),
    path('new/project/', views.new_project, name='newProject'),
    path('search/', views.search, name='search_results'),
    path('reviews/',views.reviews,name = 'reviews'),
    path('rate/<int:id>',views.rate, name='rating'),
    path("project/<int:project_id>/", views.project_review, name="project_review"),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

