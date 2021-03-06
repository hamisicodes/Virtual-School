from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.base import TemplateResponseMixin, View
from .models import Course,Subject
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import (ListView, DetailView,CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from . forms import CourseForm
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin, View
from django.utils.translation import ugettext_lazy as _
from .models import Course,Subject,Content,Module
from django.db.models import Count
from django.apps import apps
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy,reverse
from .forms import ModuleFormSet, CourseCreateForm
from django.forms.models import modelform_factory
from django import forms
from braces.views import LoginRequiredMixin, PermissionRequiredMixin,CsrfExemptMixin, JsonRequestResponseMixin
from student.forms import StudentRegistrationForm


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
    return render(request, 'index.html',{'form':form})


def is_users(subject_username, logged_user):
    return subject_username == logged_user
# Create your views here.

# def is_users(course_user, logged_user):
#     return course_user == logged_user

def home(request):
    return render(request, 'index.html')

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin,PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'course_name', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin):
    fields = ['subject', 'course_name', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'

class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'
class CourseCreateView(OwnerCourseEditMixin, OwnerEditMixin, CreateView, PermissionRequiredMixin):
    template_name = 'courses/manage/course/form.html'
    permission_required = 'courses.add_course'
class CourseUpdateView(OwnerCourseEditMixin, UpdateView, PermissionRequiredMixin):
    template_name = 'courses/manage/course/form.html'
    permission_required = 'courses.can_change'
    
class CourseDeleteView(OwnerCourseMixin, DeleteView, PermissionRequiredMixin):
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')
    permission_required = 'courses.can_delete'
    
class CreateSubject(LoginRequiredMixin,CreateView):
    model = Subject
    fields = ['title']
    permission_required = 'courses.view_subject'

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class SubjectView(ListView,LoginRequiredMixin):
    
    model = Subject
    template_name = 'content_management/subject.html'
    context_object_name = 'subjects'
    permission_required = 'subject.can_view'

class SubjectDelete(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = 'content_management/subject-delete.html'
    context_object_name = 'subject'
    success_url = reverse_lazy('subjects-list')
    permission_required = 'subject.can_delete'
    def test_func(self):
        return is_users(self.get_object().username, self.request.user)


class UpdateSubject(LoginRequiredMixin,UpdateView):
    model = Subject
    fields = ['title']
    permission_required = 'subject.change_subject'
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
    permission_required = 'courses.view_detail'
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

def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_titles = Subject.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'content_management/search.html',{"message":message,"titles": searched_titles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'content_management/search.html',{"message":message})

class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super(CourseModuleUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({ 'course': self.course, 'formset': formset })

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)

        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({ 'course': self.course, 'formset': formset })

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(initial={'course': self.object})
        return context
      

class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'courses/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file',]:
            return apps.get_model(app_label='content_management_system', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner', 'order', 'created', 'updated'], widgets={'title': forms.TextInput(attrs={'class':'form-control'}), 'content': forms.Textarea(attrs={'class':'form-control', 'cols': 40, 'rows': 8}), 'url': forms.TextInput(attrs={'class':'form-control'})})

        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(Module, id=module_id, course__owner=request.user)
        self.model = self.get_model(model_name)

        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)

        return super(ContentCreateUpdateView, self).dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({ 'form':form, 'object': self.obj })
    
    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                Content.objects.create(module=self.module, item=obj)
            return redirect('module_content_list', self.module.id)

        return self.render_to_response({ 'form': form, 'object': self.obj })


class ContentDeleteView(View):

    def post(self, request, id):
        content = get_object_or_404(Content, id=id, module__course__owner=request.user)
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('module_content_list', module.id)

class ModuleContentListView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/content_list.html'

    def get(self, request, module_id):
        module = get_object_or_404(Module, id = module_id, course__owner = request.user)

        return self.render_to_response({'module': module})



class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'courses/course/list.html'

    def get(self, request, subject=None):
        subjects = cache.get('all_subjects')
        if not subjects:
            subjects = Subject.objects.annotate(
                            total_courses=Count('course'))
            cache.set('all_subjects', subjects)
        all_courses = Course.objects.annotate(
                           total_modules=Count('modules'))
        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            key = f'subject_{subject.id}_courses'
            courses = cache.get(key)
            if not courses:
                courses = all_courses.filter(subject=subject)
                cache.set(key, courses)
        else:
            courses = cache.get('all_courses')
            if not courses:
                courses = all_courses
                cache.set('all_courses', courses)
        return self.render_to_response({'subjects': subjects,
                                        'subject': subject,
                                        'courses': courses})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(
                                   initial={'course':self.object})
        return context

class ModuleOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):

    def post(self, request):
        for id, order in self.request_json.items():
            Module.objects.filter(id=id,
                                  course__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})


class ContentOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):

    def post(self, request):
        for id, order in self.request_json.items():
            Content.objects.filter(id=id,
                                   module__course__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})