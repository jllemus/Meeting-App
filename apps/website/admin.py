from django.contrib import admin
from .models import Meeting, Room, Notification
# Register your models here.
admin.site.register(Meeting)
admin.site.register(Room)
admin.site.register(Notification)

