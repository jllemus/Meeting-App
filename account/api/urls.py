from django.urls import path, include
from account.api.views import registration_view

app_name = 'account'

urlpatterns = [
    ## REST DJANGO API
    path('register/', registration_view, name="account_api"),
]