from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile
from content_management_system.models import Course
class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['image', 'bio']

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
    widget=forms.HiddenInput)        