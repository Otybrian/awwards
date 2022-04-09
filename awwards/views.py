from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, UserProfileForm, RateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile, Project, Rating, Review
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404
from collections import UserString
from django.contrib.messages import constants as messages
# Create your views here.

def home(request):
    project = Project.objects.all().order_by('-id')
    return render(request, 'home.html',{'projects':project})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {"form":form,'projects':project,'profile':profile})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Project.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'images': images})
    else:
        message = 'Not found'
    return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login/')
def rate(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design_rate = request.POST['design']
        content_rate = request.POST['content']
        usability_rate = request.POST['usability']
        Rating.objects.create(project=project,user=current_user,design_rate=design_rate,usability_rate=usability_rate,content_rate=content_rate,average=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2),)

        return render(request,"project_review.html",{"project":project})
    else:
        project = Project.objects.get(id = id) 
        return render(request,"project.html",{"project":project})
