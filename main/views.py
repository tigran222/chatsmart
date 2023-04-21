from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, MessageForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Room, Message
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	user = request.user
	rooms = Room.objects.filter(users=user)
	return render(request, 'main/index.html', context={'username': user, 'rooms': rooms})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

# def room(request, room_id):
#     room = get_object_or_404(Room, pk=room_id)
#     messages = Message.objects.filter(room=room)
#     return render(request, 'main/room.html', {'room': room, 'messages': messages})

@login_required
def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    messages = Message.objects.filter(room=room)
    if request.method == 'POST':
    	form = MessageForm(request.POST)
    	if form.is_valid():
    		message = form.save(commit=False)
    		message.room = room
    		message.user = request.user
    		message.save()
    		form = MessageForm()
    else:
    	form = MessageForm()

    messages = Message.objects.filter(room=room)
    if room.is_private and room.password:
        return redirect('room_password', room_id=room.pk)

    return render(request, 'main/room.html', {'room': room, 'messages': messages}) 

     
@login_required
def room_password(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        entered_password = request.POST.get('password')
        if entered_password == room.password:
            request.session['room_id'] = room_id
            return redirect('room', room_id)
        else:
            message = 'Invalid password. Please try again.'
    else:
        message = ''

    return render(request, 'main/room_password.html', {'room': room, 'message': message})


# @csrf_exempt
# def send_message(request):
# 	if request.method == 'POST':
# 		form = MessageForm(request.POST)
# 		if form.is_valid():
# 			return JsonResponse({'success': True})
# 	else:
# 		return JsonResponse({'success': False})


# @csrf_exempt
# def get_messages(request, room_id):
#     room = get_object_or_404(Room, pk=room_id)
#     messages = Message.objects.filter(room=room).order_by('-created_at')[:50][::-1]
#     message_list = []
#     for message in messages:
#         message_list.append({'id': message.pk, 'content': message.content, 'username': message.user.username, 'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S')})

#     return JsonResponse({'messages': message_list})
