from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser




# Create your models here.

class Room(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(default='new room')
	is_private = models.BooleanField(default=False)
	password = models.CharField(max_length=255, null=True, blank=True)
	users = models.ManyToManyField(User, related_name='members')

	def __str__(self):
		return self.name 

# class User(AbstractUser):
#     rooms = models.ManyToManyField(Room, related_name='members')

class Message(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content

