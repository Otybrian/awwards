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
from django.contrib.messages import constants as messages
# Create your views here.

def home(request):
    photo = Project.objects.all().order_by('-id')
    return render(request, 'home.html',{'photo':photo})

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)


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


