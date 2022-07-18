from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.sign_up, name='sign_up'),
    path('mentor', views.mentor_up, name='mentor_up'),
    path('homeroom', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]