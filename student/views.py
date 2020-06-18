from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def student_register(request):
    form = UserCreationForm()
    return render(request, 'student/register.html',{'form':form})