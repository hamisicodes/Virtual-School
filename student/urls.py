from django.urls import path
from . import views as student_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('student_register', student_views.student_register, name='student_register'),
    path('student_profile/', student_views.student_profile, name = 'student_profile'),
    path('login/', views.studentLogin, name = 'login'),
    path('dashboard/',views.dashboard , name= 'dashboard'),
    path('modules/(<int:pk>)/',views.module_list , name= 'module_list'),

]