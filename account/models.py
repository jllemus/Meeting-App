from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_image', blank=True)
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
<<<<<<< HEAD
        Profile.objects.create(user=instance)
=======
        Profile.objects.create(user_name=instance)
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
