
from django.urls import path

from users.views import loginMain, profile

app_name = 'users'

urlpatterns = [
    path('loginMain/', loginMain, name='loginMain'),
    path('profile/', profile, name='profile')
] 
