from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.sign_up, name='sign_up'),
    path('mentorup', views.mentor_up, name='mentor_up'),
    path('chat', views.chat, name='chat'),
]