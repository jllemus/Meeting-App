from django.urls import path
from .views import Account, ChangePassword, EditAccount

app_name = 'account'
urlpatterns = [
    path('account_info/', Account.as_view(), name='account_view'),
    path('edit_account/', EditAccount.as_view(), name='edit_account_view'),
    path('edit_account/change_password/', ChangePassword.as_view(), name='change_password_view')
]

