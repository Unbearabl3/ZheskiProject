from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from .models import User
from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def reg(request):
    return render(request, 'users/reg.html')
def authorization(request):
    return render(request, 'users/authorization.html')
def loginMain(request):
    if request.method == 'POST':
        formReg = UserRegistrationForm(data=request.POST)
        form = UserLoginForm(data=request.POST)
        if formReg.is_valid():
            formReg.save()
            return HttpResponseRedirect(reverse('users:loginMain'))
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
        formReg = UserRegistrationForm()

    context = {'formReg': formReg, 'form': form}
    return render(request, 'users/loginMain.html', context)
def prototype(request):
    return render(request, 'users/prototype.html')