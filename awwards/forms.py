from django import forms
from .models import Rating, RATE_CHOICES, Project, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'photo','link', 'description')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['profile_pic', 'location', 'bio']


class RateForm(forms.ModelForm):
    design = forms.ChoiceField(choices = RATE_CHOICES, widget=forms.Select(), required=True)
    content = forms.ChoiceField(choices = RATE_CHOICES, widget=forms.Select(), required=True)
    usability = forms.ChoiceField(choices = RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Rating
        fields = ('design', 'content', 'usability')
