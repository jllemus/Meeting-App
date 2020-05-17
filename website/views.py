from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
<<<<<<< HEAD
from django.views.generic import TemplateView
from django import forms
from website.forms import MeetingForm
from website.models import Meeting


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
        args = {'data': data, 'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        """
        Saves new meetings from the template into the meeting model.
        """
        updated_request = request.POST.copy()
        updated_request.update({'added_by':request.user.username})
        form = MeetingForm(updated_request) 
        if form.is_valid():
            form.save()
            return redirect("website:meeting_view")
        else:
            form = MeetingForm()
        ## All the above can also be done by creating a form from the MeetingForm, pass 
        ## The request and then modify the cleaned_data field.

@method_decorator(login_required, name='post')
class EditMeeting(TemplateView):
    
    def post(self, request, action, id):
        """
        Method to take commands from the template. 
        deletes and updates meeting from the meeting template.
        """
        if action == 'delete':
            obj = get_object_or_404(Meeting, pk=id)
            obj.delete()
            return redirect('website:meeting_view')
        elif action == 'save':
            instance = Meeting.objects.get(pk=id)
            form = MeetingForm(request.POST, instance=instance)
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
=======
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

## REST FRAMEWORK
from rest_framework import viewsets  
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.forms import  MeetingForm
from website.models import Meeting
from website.serializer import MeetingSerializer 

@api_view(['GET',])
def meeting_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    try:
        meetings = Meeting.objects.all()
    except Meeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = MeetingSerializer(meetings, many= True)
        return Response(serializer.data)



@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ManageMeeting(TemplateView):
    template_name = 'website/meeting.html'
    def get(self, request):
        data = Meeting.objects.filter(added_by__username__contains=request.user) ##Filtering objects with ForeignKey is different
        form = MeetingForm()
        args = {'data': data, 'form': form}
        return render(request, self.template_name, args)
    def post(self, request):
        if request.method == "POST":
            form = MeetingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("website:meeting_view")
            else:
                form = MeetingForm()

@method_decorator(login_required, name='post')
class DeleteMeeting(TemplateView):
    def post(self, request, action, id):
        if request.method == "POST":
            if action == 'delete':
                obj = get_object_or_404(Meeting, pk=id)
                obj.delete()
                return redirect('website:meeting_view')
            elif action == 'save': 
                form = MeetingForm(request.POST)
                if form.is_valid():
                    instance = Meeting.objects.get(pk=id)
                    form_data = MeetingForm(request.POST, instance=instance)
                    form_data.save()
                    return redirect("website:meeting_view")

class Register(TemplateView):
    template_name='website/signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'website/signup.html', {'form': form})
    
    def post(self, request):
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:user_login')

<<<<<<< HEAD

def welcome(request):
    return render(request, 'website/welcome.html', {'data': json_search})

=======
def welcome(request):
    return render(request, 'website/welcome.html')
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
