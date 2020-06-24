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
  path('jimbo/', views.CourseListView.as_view(), name='course_list'),
  path('',views.home,name='index'),
  path('create/', views.CourseCreateView.as_view(),
        name='course_create'),
  path('<int:pk>/edit', views.CourseUpdateView.as_view(),
        name='course_edit'),
  path('<int:pk>/delete', views.CourseDeleteView.as_view(),
        name='course_delete'),
  path('<int:pk>/module', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
  path('mine/', views.ManageCourseListView.as_view(),
        name='manage_course_list'),
  path('new/subject', CreateSubject.as_view(template_name = 'content_management/create_subject.html'), name = 'create-subject'),
  path('subject/', SubjectView.as_view(template_name = 'content_management/subject.html'), name = 'subjects-list'),
  path('subject/<int:pk>/update', UpdateSubject.as_view(template_name = 'content_management/subject_update.html'), name = 'subject-update'),
  path('subject/<int:pk>/delete',SubjectDelete.as_view(), name = 'subject-delete'),
  path('subject/<int:pk>/', SubjectDetail.as_view(), name = 'subject-detail'),
  path('content/<int:id>/delete', views.ContentDeleteView.as_view(), name='module_content_delete'),
  path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
  path('subject/<subject>/', views.CourseListView.as_view(), name='course_list_subject'),
  path('<int:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
  path('module/<int:module_id>/content/<model_name>/create/',
    views.ContentCreateUpdateView.as_view(),
    name='module_content_create'),
  path('module/<int:module_id>/content/<model_name>/<int:id>/',
    views.ContentCreateUpdateView.as_view(), 
    name='module_content_update'),




]