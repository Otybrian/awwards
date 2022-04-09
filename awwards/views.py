from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, UserProfileForm, RateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile, Project
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
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {"form":form,'projects':project,'profile':profile})


@login_required(login_url='/accounts/login/')
def newProject(request):
    current_user = request.user
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            form.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {"form": form})


