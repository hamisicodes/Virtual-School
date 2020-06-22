from django.urls import path,include
from . import views
from .views import CourseCreateView,CourseUpdateView,CourseDeleteView
from .views import CreateSubject,SubjectView,SubjectDelete,UpdateSubject,SubjectDetail
from django.contrib.auth import views as auth_views
# from .models import Course


urlpatterns=[
  # path('new/course', CreateCourse.as_view(template_name = 'create_course.html'), name = 'create-course'),
  # path('', CourseView.as_view(template_name = 'course_view.html'), name = 'courses-list'),
  # path('course/<int:pk>/update', UpdateCourse.as_view(template_name = 'update_course.html'), name = 'course-update'),
  # path('course/<int:pk>/delete',DeleteCourse.as_view(), name = 'course-delete'),
  path('create/', views.CourseCreateView.as_view(),name='course_create'),
  path('<int:pk>/edit', views.CourseUpdateView.as_view(),name='course_edit'),
  path('<int:pk>/delete', views.CourseDeleteView.as_view(),name='course_delete'),
  path('mine/', views.ManageCourseListView.as_view(),name='manage_course_list'),
  path('new/subject', CreateSubject.as_view(template_name = 'content_management/create_subject.html'), name = 'create-subject'),
  path('', SubjectView.as_view(template_name = 'content_management/subject.html'), name = 'subjects-list'),
  path('subject/<int:pk>/update', UpdateSubject.as_view(template_name = 'content_management/subject_update.html'), name = 'subject-update'),
  path('subject/<int:pk>/delete',SubjectDelete.as_view(), name = 'subjects-list'),
  path('subject/<int:pk>/', SubjectDetail.as_view(), name = 'subject-detail'),
  path('search/', views.search_results, name='search_results'),
]