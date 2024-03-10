from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'FormAuthorization_Data_UserName_Input', 'placeholder':'Имя Пользователя',
        'id': 'FormAuthorization_Data-Form_Input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'FormAuthorization_Data_Password_Input', 'placeholder':'Пароль',
        'id': 'FormAuthorization_Data-Form_Input'
    }))

    class Meta:
        model = User
        fields = ('UserName', 'Password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'FormRegistration_Data_UserName_Input', 'placeholder':'Имя Пользователя',
        'id': 'FormRegistration_Data-Form_Input'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'FormRegistration_Data_Mail_Input', 'placeholder':'E-mail',
        'id': 'FormRegistration_Data-Form_Input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'FormRegistration_Data_Password_Input', 'placeholder':'Пароль',
        'id': 'FormRegistration_Data-Form_Input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'FormRegistration_Data_Password-Replay_Input', 'placeholder':'Подтвердите пароль',
        'id': 'FormRegistration_Data-Form_Input'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')