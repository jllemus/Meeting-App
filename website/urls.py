from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from website.views import ManageMeeting, EditMeeting, welcome, Register
from website.api.views import GetToken
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'website'

urlpatterns = [
    path('meeting/', ManageMeeting.as_view(), name='meeting_view'),
    path('register/', Register.as_view(), name='user_signup'),
    path('login/', LoginView.as_view(template_name='website/login.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('get_token/', GetToken.as_view(), name="get_token"),
    path('delete_item/<str:action>/<int:id>', EditMeeting.as_view(), name="edit_view"),
    path('', welcome, name="welcome_view"),
]
