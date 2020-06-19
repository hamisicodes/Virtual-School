from .forms import CourseForm
from django.shortcuts import render,redirect,get_object_or_404 
from django.contrib.auth.models import User
from .models import Subject,Course
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def is_users(subject_user, logged_user):
    return subject_user == logged_user


class CreateSubject(LoginRequiredMixin,CreateView):
    model = Subject
    fields = ['title','slug']
    

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class SubjectView(ListView):
    
    model = Subject
   
    template_name = 'content_management/subject.html'
    context_object_name = 'subjects'

class SubjectDelete(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = 'content_management/subject-delete.html'
    context_object_name = 'subject'
    success_url = '/'
    
    def test_func(self):
        return is_users(self.get_object().username, self.request.user)

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'content_management/course-delete.html'
    context_object_name = 'course'
    success_url = '/'

class UpdateSubject(LoginRequiredMixin,UpdateView):
    model = Subject
    fields = ['title','slug']
    def test_func(self):
        subject = self.get_object()
        if self.request.username == subject.user:
            return True
        return False


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class SubjectDetail(DetailView):
    model = Subject
    template_name = 'content_management/subject-detail.html'
    context_object_name = 'subject'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        courses_connected = Course.objects.filter(subjects=self.get_object()).order_by('-date_posted')
        data['courses'] = courses_connected
        data['form'] = CourseForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_course = Course(course_slug=request.POST.get('course_slug'),
                            course_title=request.POST.get('course_title'),
                            overview=request.POST.get('overview'),
                            username=self.request.user,
                            subjects=self.get_object())

        new_course.save()

        return self.get(self, request, *args, **kwargs)

class CourseDelete(LoginRequiredMixin, DeleteView):
              model = Course
              template_name = 'content_management/course-delete.html'
              context_object_name = 'course'
              success_url = '/'

class UpdateCourse(LoginRequiredMixin,UpdateView):
              model = Course
              fields = ['course_title','course_slug','overview']
              def form_valid(self,form):
                 form.instance.username = self.request.user
                 return super().form_valid(form)
                 