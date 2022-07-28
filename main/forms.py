from email.policy import default
from pyexpat import model
from selectors import DefaultSelector
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from numpy import require
import pandas as pd
import os
from requests import request
from .models import MatchForm, Registration, login
from django.forms import ModelForm

         
class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    University = forms.CharField(required=False)
    Department = forms.CharField(required=False)
    State = forms.CharField(required=False)
    City = forms.CharField(required=False)

    class Meta:
        model = Registration
        fields = '__all__'

class match_form(ModelForm):

    class Meta:
        model = MatchForm
        fields = '__all__'

class login_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style':'max-width: 24em'}))
    email = forms.EmailField(
    max_length=64,
    widget=forms.TextInput(attrs={'style':'max-width: 24em'}),
    required=True)
    

    class Meta:
        model = login
        fields = '__all__'
