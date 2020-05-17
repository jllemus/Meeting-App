from django.urls import path, include
from website.api.views import MeetingApi, GetToken

app_name = 'website'

urlpatterns = [
    ## REST DJANGO API
    path('', MeetingApi.as_view(), name="meeting_api"),
]
