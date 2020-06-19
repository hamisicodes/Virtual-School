from django import forms
from django.contrib.auth.models import User
from .models import Course,Subject

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_title','course_slug','overview']
