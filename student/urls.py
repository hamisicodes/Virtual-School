from django.urls import path
from . import views as student_views

urlpatterns = [
    path('student_register', student_views.student_register, name='student_register'),
    path('student_profile/', student_views.student_profile, name = 'student_profile'),
]