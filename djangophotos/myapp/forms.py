from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Photo
from datetime import date

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['date', 'photo']
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}),
        }