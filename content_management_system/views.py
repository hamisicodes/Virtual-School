from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404 
from django.contrib.auth.models import User
from .models import Subject
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
    
    # def test_func(self):
    #     return is_users(self.get_object().user, self.request.user)

class UpdateSubject(LoginRequiredMixin,UpdateView):
    model = Subject
    fields = ['title','slug']
    # def test_func(self):
    #     subject = self.get_object()
    #     if self.request.user == subject.user:
    #         return True
    #     return False


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



