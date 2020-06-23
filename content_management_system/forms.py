from django import forms
from django.contrib.auth.models import User
from .models import Course,Subject,Content,Module
from django.forms.models import inlineformset_factory



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name','slug','overview']
class ModuleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 40, 'rows': 8}))

    class Meta:
        model = Module
        exclude = ()

ModuleFormSet = inlineformset_factory(Course, Module, form=ModuleForm, fields=['title', 'description',], extra=2, can_delete=True)



class CourseCreateForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    overview = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 40, 'rows': 15}))

    class Meta:
        model = Course
        fields = ['subject', 'course_name', 'overview']