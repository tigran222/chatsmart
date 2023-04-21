from django.urls import path 
from . import views 

urlpatterns=[
	path('', views.index, name='index'),
	path('login/', views.login_request, name='login'),
	path('register/', views.register_request, name='register'),
	path('logout/', views.logout_request, name='logout'),
	path('room/<int:room_id>', views.room, name='room'),
	path('room/<int:room_id>/password/', views.room_password, name='room_password'),
	path('send-message/', views.send_message, name='send_message'),
  	path('get-messages/', views.get_messages, name='get_messages')

]