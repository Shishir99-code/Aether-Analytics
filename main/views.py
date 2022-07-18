from django.shortcuts import redirect, render
from requests import request
from .forms import RegisterForm, MentorshipForm, ChatForm, RegistrationForm
from django.contrib.auth import login, logout, authenticate
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form1': form}
    return render(request, 'registration/sign_up.html', context)

def mentor_up(request):
    form = MentorshipForm()
    if request.method == 'POST':
        form = MentorshipForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form2': form}
    return render(request, 'registration/mentor_up.html', context)

def chat(request):
    return render(request, 'chat/room.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/chat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

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

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
