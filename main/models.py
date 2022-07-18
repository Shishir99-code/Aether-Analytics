from django.db import models
from datetime import datetime

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