from django import forms
from .models import Rating,Review, RATE_CHOICES, Project, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea

        
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'image','description','link']
        widgets = {
            'description': Textarea(attrs={'cols' : 20, 'rows' : 5}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','contact']
        widgets = {
            'bio': Textarea(attrs={'cols': 30, 'rows': 3}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['design_rate','usability_rate','content_rate']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['review']
