from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from django.forms import ModelForm

class UpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', ) 