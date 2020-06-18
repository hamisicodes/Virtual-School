from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import StudentRegistrationForm
from .models import StudentProfile

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save(0)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Student Account created for {username}')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student/register.html',{'form':form})

def student_profile(request):
    profile = StudentProfile.objects.get_or_create(user=request.user)
    context = {
        'profile':profile
    }
    return render(request, 'student/profile.html', context)