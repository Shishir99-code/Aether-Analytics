from django.shortcuts import redirect, render
from requests import request
from .forms import RegisterForm, MentorshipForm, ChatForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/mentorup')
    else: 
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def mentor_up(request):
    if request.method == 'POST':
        form_two= MentorshipForm(request.POST)
        if form_two.is_valid():
            user = form_two.save()
            login(request, user)
            return redirect('/home')
    else:
        form_two = MentorshipForm()

    return render(request, 'registration/mentor_up.html', {"form2": form_two})

def chat(request):
    return render(request, 'main/chat.html')

def find(request):
    if request.method == 'POST':
        form_3= ChatForm(request.POST)
        if form_3.is_valid():
            user = form_3.save()
            login(request, user)
            return redirect('/chat')
    else:
        form_3 = ChatForm()

    return render(request, 'main/home.html', {"form3": form_3})