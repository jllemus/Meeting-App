from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
<<<<<<< HEAD
from website.views import ManageMeeting, EditMeeting, welcome, Register
from website.api.views import GetToken
from rest_framework.authtoken.views import obtain_auth_token


=======
from .views import meeting_view, ManageMeeting, DeleteMeeting, welcome, Register
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
app_name = 'website'

urlpatterns = [
    path('meeting/', ManageMeeting.as_view(), name='meeting_view'),
    path('register/', Register.as_view(), name='user_signup'),
    path('login/', LoginView.as_view(template_name='website/login.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
<<<<<<< HEAD
    path('get_token/', GetToken.as_view(), name="get_token"),
    path('delete_item/<str:action>/<int:id>', EditMeeting.as_view(), name="edit_view"),
    path('', welcome, name="welcome_view"),
=======
    path('delete_item/<str:action>/<int:id>', DeleteMeeting.as_view(), name="delete_view"),
    path('', welcome, name="welcome_view"),


    ## REST DJANGO API
    path('api/', meeting_view, name="meeting_api"),
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
]
