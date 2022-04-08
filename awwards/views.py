from django.shortcuts import render
from awwards.email import send_welcome_email

# Create your views here.

def home(request):
    return render(request, 'home.html')

