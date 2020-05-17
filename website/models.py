from django.db import models
from django.conf import settings
from datetime import time
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__ (self):
        return f"{self.name}, in floor number {self.floor_number} and room number {self.room_number}"


class Meeting(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=300, blank=True)
    date = models.DateField(blank=True)
    start_time = models.TimeField(default = time(9), blank=True)
    duration = models.IntegerField(default = 1, blank=True)
    #added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    added_by = models.CharField(max_length=20, default='----')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True)
=======
    title = models.CharField(max_length=300)
    date = models.DateField()
    start_time = models.TimeField(default = time(9))
    duration = models.IntegerField(default = 1)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
