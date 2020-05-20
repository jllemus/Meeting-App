from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:user_login')

def welcome(request):
    return render(request, 'website/welcome.html')
