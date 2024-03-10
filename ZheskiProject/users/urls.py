
from django.urls import path

from users.views import loginMain

app_name = 'users'

urlpatterns = [
    path('loginMain/', loginMain, name='loginMain'),
] 
