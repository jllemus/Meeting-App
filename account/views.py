from django.shortcuts import render, redirect
from django.views.generic import TemplateView   
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import update_session_auth_hash
from .forms import UpdateProfile, ProfileForm
from account.models import Profile

# Create your views here.

@method_decorator(login_required, name='get')
class Account(TemplateView):
    template_name = "account/account_info.html"

    def get(self, request):
        return render(request, self.template_name)

@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class EditAccount(TemplateView):
    template_name = 'account/edit_account_info.html'

    def get(self, request):
        image_instance = Profile.objects.get(user=request.user)
        user_instance = User.objects.get(username=request.user)

        form = UpdateProfile(instance=user_instance)
        image_form = ProfileForm(instance=image_instance)
        
        return render(request, self.template_name, {'form':form, 'image_form':image_form})


    def post(self, request):
        image_instance = Profile.objects.get(user=request.user)
        user_instance = User.objects.get(username=request.user)

        form = UpdateProfile(request.POST, instance=user_instance)
        image_form = ProfileForm(request.POST, request.FILES, instance=image_instance)
        if form.is_valid() and image_form.is_valid():
            form.save()
            image_form.save()
            return redirect('account:account_view')

@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ChangePassword(TemplateView):
    template_name="account/change_password.html"

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
<<<<<<< HEAD
        form = PasswordChangeForm(data=request.POST, user=request.user)
=======
        form = PasswordChangeForm(request.POST, user=request.user)
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
        if form.is_valid():
            form.save()
            #This is to keep logged in sesion
            update_session_auth_hash(request, form.user)
            return redirect('account:account_view')
        else:
            return redirect('account:change_password_view')
    
