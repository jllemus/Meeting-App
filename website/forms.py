from django.forms import ModelForm, modelform_factory
from .models import Meeting
## This is a more organized way to do this, however, you can simply 
## go to views.py file and import the modelform_factory method
## this will help to import a model form class of the model database, in this case I named it "MeetingForm"
## Example:
## from django.forms import modelform_factory
## MeetingForm = modelform_factory(ModelName, exclude=[])
## and the MeetingForm class, now can be used in any view function in the views.py file

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
