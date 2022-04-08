from django import forms
from .models import Rating, RATE_CHOICES


class RateForm(forms.ModelForm):
    design = forms.ChoiceField(choices = RATE_CHOICES, widget=forms.Select(), required=True)
    content = forms.ChoiceField(choices = RATE_CHOICES, widget=forms.Select(), required=True)
    usability = forms.ChoiceField(choices = RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Rating
        fields = ('design', 'content', 'usability')
