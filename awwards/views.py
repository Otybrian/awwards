from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from awwards.email import send_welcome_email
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, UserProfileForm, RateForm, SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from django.contrib.auth import login, authenticate
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})

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
