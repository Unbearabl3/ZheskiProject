from django.shortcuts import render

# Create your views here.
def reg(request):
    return render(request, 'users/reg.html')
def authorization(request):
    return render(request, 'users/authorization.html')