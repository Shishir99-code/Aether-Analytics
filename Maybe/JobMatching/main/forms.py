from email.policy import default
from selectors import DefaultSelector
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from numpy import require
import pandas as pd
import os
from requests import request

from sqlalchemy import except_, null

CHOICES = [
    ('Limited', 'LIMITED'),
    ('Moderate', 'MODERATE'),
    ('Free', 'FREE'),
    ]

YEARS = [
    ('Years', 'Years'),
    ('0-1', '0-1'),
    ('1-2', '1-2'),
    ('2-3', '2-3'),
    ('3-4', '3-4'),
    ('4-5', '4-5'),
    ('5+', '5+'),
]

df_location = pd.read_csv("Data/us_cities_states_counties.csv", sep='|')
df_company = pd.read_csv("Data/nasdaq-listed.csv")


print("here")

# Dictionaries for all states and cities
unique_states = pd.unique(df_location['State full'].sort_values())
states_dictionary = list(map(lambda x, y:(x,y), unique_states, unique_states))
unique_cities = pd.unique(df_location['City'].sort_values())
cities_dictionary = list(map(lambda x, y:(x,y), unique_cities, unique_cities))

unique_company = pd.unique(df_company['Company Name'].sort_values())
company_dictionary = list(map(lambda x, y:(x,y), unique_company, unique_company))


COMPANY = company_dictionary
STATE = states_dictionary
CITIES = cities_dictionary


class RegisterForm(UserCreationForm):
    username = forms.CharField(label= 'Email')
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    University = forms.CharField(label='University(Current/Alumni)', required=True)
    #Company = forms.CharField(max_length=100)
    #position = forms.CharField(max_length=200)
    #department = forms.CharField(max_length=200)
    #state = forms.CharField(max_length=100)
    #city = forms.CharField(max_length=100)
    #PastExperiences = forms.CharField(label="Past Company Experiences")
    #Availablity = forms.CharField(label='What is your availability?',
#widget = forms.Select(choices=CHOICES))
    
    class Meta:
        model = User
        fields = ['username']

    
class MentorshipForm(forms.ModelForm):
    Company = forms.CharField(max_length=100, required=False,
widget = forms.Select(choices=COMPANY))
    Position = forms.CharField(max_length=200, required=False,)
    Department = forms.CharField(max_length=200, required=False,)
    State = forms.CharField(max_length=100, required=False,
widget = forms.Select(choices=STATE), )
    City = forms.CharField(max_length=100, required=False,
widget = forms.Select(choices=CITIES)) 
    username = forms.CharField(label='Years of Experience', required=False,
widget = forms.Select(choices=YEARS))


    class Meta:
        model = User
        fields = ['username']

class ChatForm(forms.ModelForm):
    Company = forms.CharField(max_length=100, required=False,
widget = forms.Select(choices=COMPANY))

    class Meta:
        model = User
        fields = ['username']
