from django.db import models
from datetime import datetime
import pandas as pd

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




# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

class Registration(models.Model):
    email = models.EmailField(max_length=60)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    University = models.CharField(max_length=60)

class Mentoration(models.Model):
    Years_of_Experience = models.CharField(max_length=60, choices=YEARS, default='1-2')
    Company = models.CharField(max_length=100, choices=COMPANY, default='#Enter Company')
    Position = models.CharField(max_length=60)
    Department = models.CharField(max_length=60)
    State = models.CharField(max_length=60, choices=STATE, default='#Enter State')
    City = models.CharField(max_length=60, choices=CITIES, default='#Enter City')