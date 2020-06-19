from django import forms
from django.contrib.auth.models import User
from .models import Course,Subject
# from django.forms.models import inlineformset_factory
# from .models import Course, Module


# ModuleFormSet = inlineformset_factory(Course,
#                                       Module,
#                                       fields=['title', 'description'],
#                                       extra=2,
#                                       can_delete=True)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name','slug','overview']
