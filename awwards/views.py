from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from awwards.email import send_welcome_email
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, UserProfileForm, RateForm 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from django.contrib.auth import login, authenticate
# Create your views here.

def home(request):
    photo = Project.objects.all().order_by('-id')
    return render(request, 'home.html',{'photo':photo})

@login_required(login_url='/accounts/login/')
def newProject(request):
    if request.method == 'POST':
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=ProjectForm()
    return render(request, 'new_project.html', {'form': form})
