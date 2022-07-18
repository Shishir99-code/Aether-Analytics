from django.contrib import admin
from .models import Mentoration, Room, Message, Registration


# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Registration)
admin.site.register(Mentoration)