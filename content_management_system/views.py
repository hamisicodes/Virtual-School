from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.base import TemplateResponseMixin, View
from .models import Course,Subject
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from . forms import CourseForm

# Create your views here.

# def is_users(course_user, logged_user):
#     return course_user == logged_user

def home(request):
    subjects = Subjects.objects.all()
    return render(request, 'home.html', {'subjects' : subjects})

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course
    fields = ['subject', 'course_name', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin):
    fields = ['subject', 'course_name', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'

class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'

class CourseCreateView(OwnerCourseEditMixin, OwnerEditMixin, CreateView, PermissionRequiredMixin):
    template_name = 'courses/manage/course/form.html'
    permission_required = 'courses.can_add'

class CourseUpdateView(OwnerCourseEditMixin, UpdateView, PermissionRequiredMixin):
    template_name = 'courses/manage/course/form.html'
    permission_required = 'courses.can_change'

class CourseDeleteView(OwnerCourseMixin, DeleteView, PermissionRequiredMixin):
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')
    permission_required = 'courses.can_delete'





# def is_users(course_user, logged_user):
#     return course_user == logged_user


# class CreateCourse(LoginRequiredMixin, CreateView):
#     model = Course
#     fields = ['course_name','overview','slug','subject']

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class CourseView(ListView):
    
#     model = Course
   
#     template_name = 'course_view.html'
#     context_object_name = 'course'

# class UpdateCourse(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Course
#     fields = ['course_name','overview','slug','subject']

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

    # def test_func(self):
    #     course_name = self.get_object()
    #     if self.request.user == course_name.user:
    #         return True
    #     return False

# class DeleteCourse(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Course
#     sucess_url = '/'
#     template_name ='delete_course.html'
#     context_object_name = 'course'

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

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
        courses_connected = Course.objects.filter(subject=self.get_object()).order_by('-created')
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



