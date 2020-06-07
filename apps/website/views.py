from django.shortcuts import render, redirect, HttpResponse, Http404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404
from django import forms
from django.http import JsonResponse
from apps.website.forms import MeetingForm
from apps.website.models import Meeting
from apps.website.models import Notification

import json

@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ManageMeeting(TemplateView):
    """
    Class to render data (meetings) from Meeting model and 
    save new meetings from the template to the database model.
    """
    template_name = 'website/meeting.html'
    def get(self, request):
        """
        Gets objects from data base model, filters them by logged user
        and then renders the data to the template.
        """
        data = Meeting.objects.filter(added_by=request.user)
        form = MeetingForm()
        form.fields['added_by'].widget = forms.HiddenInput() #Hide unnecesary field django 
        username = request.user.get_username()
        args = {'data': data, 'form': form, 'initial':username[0]}
        return render(request, self.template_name, args)

    def post(self, request):
        """
        Saves new meetings from the template into the meeting model.
        """
        updated_request = request.POST.copy()
        updated_request.update({'added_by':request.user.username})
        request_dict = dict(updated_request)
        self.save_notification(request_dict)
        form = MeetingForm(updated_request) 
        if form.is_valid():
            form.save()
            return redirect("website:meeting_view")
        else:
            form = MeetingForm()
        ## All the above can also be done by creating a form from the MeetingForm, pass 
        ## The request and then modify the cleaned_data field.

    def save_notification(self, queryset):
            """ 
            Saves notification to database based on a user passed
            """
            array = queryset['guest']
            try:
                if len(array) >= 1:
                    for item in array:
                        user = User.objects.filter(id=item)
                        notification = Notification(user=user[0], message="You have a new notification")
                        notification.save()
            except:
                raise Http404
                    
@method_decorator(login_required, name='post')
class EditMeeting(TemplateView):
    
    def post(self, request, action, id):
        """
        Method to take commands from the template. 
        deletes and updates meeting from the meeting template.
        """
        if action == 'delete':
            obj = get_object_or_404(Meeting, pk=int(id))
            obj.delete()
            return redirect('website:meeting_view')
        elif action == 'save':
            instance = Meeting.objects.get(pk=id)
            updated_request = request.POST.copy()
            updated_request.update({'added_by':request.user.username})
            form = MeetingForm(updated_request, instance=instance)
            if form.is_valid():
                form.save()
                return redirect("website:meeting_view")
    
class Register(TemplateView):
    """
    Class designed to render all the register forms 
    and save all the registered users.
    """
    template_name = 'website/signup.html'

    def get(self, request):
        """
        Renders the UserCreationForm into the template
        """
        form = UserCreationForm()
        return render(request, 'website/signup.html', {'form': form})

    def post(self, request):
        """
        Gets the data from the form in the template, and then saves it in the 
        user model.
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:user_login')

def welcome(request):
    return render(request, 'website/welcome.html')

def validate_data(request):
    if request.method == 'GET':
        info = "Heelllloooo"
        data = json.dumps(info)
        return HttpResponse(data, content_type='application/json')