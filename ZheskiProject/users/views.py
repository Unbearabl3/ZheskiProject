from django.shortcuts import render

# Create your views here.
def reg(request):
    return render(request, 'users/reg.html')
def authorization(request):
    return render(request, 'users/authorization.html')
def loginMain(request):
    return render(request, 'users/loginMain.html')
def prototype(request):
    return render(request, 'users/prototype.html')