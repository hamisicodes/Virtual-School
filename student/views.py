from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username , password= password)

        if user is not None:
            login(request,user)
            
        else:
            return render(request,'registration/login.html')
            
    return render(request,'registration/login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
