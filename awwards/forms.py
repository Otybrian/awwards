from django import forms
from .models import Rating, RATE_CHOICES, Project, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea

        
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'photo','link', 'description')
        widgets = {
            'id':'form'
        }


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
