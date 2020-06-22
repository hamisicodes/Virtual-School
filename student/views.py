from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import StudentRegistrationForm, StudentProfileUpdateForm, UserUpdateForm
from .models import StudentProfile
from content_management_system.models import Course, Module, Subject

def landing_page(request):
      return render(request, 'student/landing_page.html')

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Student Account created for {username}')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student/register.html',{'form':form})

def student_profile(request):
    profile = StudentProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form= UserUpdateForm(request.POST, instance=request.user)
        profile_form = StudentProfileUpdateForm(request.POST, request.FILES, instance=request.user.studentprofile)
        if user_form.is_valid() and  profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Profile Updated for {username}')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = StudentProfileUpdateForm(instance=request.user.studentprofile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'profile':profile,
    }
    return render(request, 'student/profile.html', context)


def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username , password= password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
            
        else:
            return render(request,'registration/login.html')
            
    return render(request,'registration/login.html')

def dashboard(request):
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    # subject_courses = Course.objects.filter(subject=pk)
    context = {
        "courses":courses,
        "subjects":subjects,
        # "subject_courses":subject_courses
    }
    return render(request, 'student/dashboard.html', context)

def module_list(request, pk):
    subjects = Subject.objects.all()
    modules = Module.objects.filter(course=pk)
    context = {
        'subjects':subjects,
        'modules':modules
    }
    return render(request, 'student/modules.html', context)

def subject_courses(request, pk):
    subject = Subject.objects.get(pk = pk)
    subjects = Subject.objects.all()
    subject_courses = Course.objects.filter(subject=subject)
    
    context = {
        'subjects':subjects,
        'subject':subject,
        'subject_courses':subject_courses
        # 'modules':modules
    }
    return render(request, 'student/subject_courses.html', context)

def my_courses(request):
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    # subject_courses = Course.objects.filter(subject=pk)
    context = {
        "courses":courses,
        "subjects":subjects,
        # "subject_courses":subject_courses
    }
    return render(request, 'student/my_courses.html', context)
