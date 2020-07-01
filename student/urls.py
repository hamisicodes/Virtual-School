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
    path('subject_courses/(<int:pk>)/',views.subject_courses , name= 'subject_courses'),
    path('my_courses/', views.my_courses , name = 'my_courses'),
    path('logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),
    path('enroll-course/',views.StudentEnrollCourseView.as_view(),name='student_enroll_course'),
    path('courses/',views.StudentCourseListView.as_view(),name='student_course_list'),
    path('course/<pk>/', views.StudentCourseDetailView.as_view(),name='student_course_detail'),
    path('course/<pk>/<module_id>/',views.StudentCourseDetailView.as_view(),name='student_course_detail_module'),
    path('enroll/<int:pk>',views.enroll,name='enroll'),
]