from django import forms
from django.forms import ModelForm

from .models import *

class task_form(forms.ModelForm):
    class Meta:
        model = task
        fields = "__all__"
    widget={
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'complete': forms.CheckboxInput(attrs={'class':'form-control'}), 
        }
