from django.contrib import admin
from .models import Room, Message

# Register your models here.

class ChatRoomAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')

admin.site.register(Room, ChatRoomAdmin)
admin.site.register(Message)
# admin.site.register(User)