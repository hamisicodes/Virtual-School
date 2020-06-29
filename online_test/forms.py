from django import forms
from django.contrib.auth.models import User
from .models import Quiz
from content_management_system.models import Course
from django.forms.models import inlineformset_factory


class QuizCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Quiz
        fields = ['name', 'course','description','roll_out']