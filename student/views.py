from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import StudentRegistrationForm, StudentProfileUpdateForm, UserUpdateForm
from .models import StudentProfile
from content_management_system.models import Course, Module, Subject
from online_test.models import Quiz

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def landing_page(request):
      return render(request, 'student/landing_page.html')

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Student Account created for {username}')
            return redirect('dashboard')
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
            messages.success(request, f'Profile Updated')
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
    # subject_courses = Course.objects.filter(subject=subjects)
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
    course = Course.objects.all()
    quizs = Quiz.objects.filter(course=course)
    
    context = {
        'subjects':subjects,
        'subject':subject,
        'subject_courses':subject_courses,
        # 'modules':modules
        'quizs':quizs
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
class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm
    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('student_course_detail',
        args=[self.course.id])
class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'student/course/list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'student/course/detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(
            id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()[0]
        return context        