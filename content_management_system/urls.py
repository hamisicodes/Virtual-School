from django.urls import path
from . import views
from .views import CourseCreateView,CourseUpdateView,CourseDeleteView
# from .models import Course


urlpatterns=[
  # path('new/course', CreateCourse.as_view(template_name = 'create_course.html'), name = 'create-course'),
  # path('', CourseView.as_view(template_name = 'course_view.html'), name = 'courses-list'),
  # path('course/<int:pk>/update', UpdateCourse.as_view(template_name = 'update_course.html'), name = 'course-update'),
  # path('course/<int:pk>/delete',DeleteCourse.as_view(), name = 'course-delete'),
  path('create/', views.CourseCreateView.as_view(),
        name='course_create'),
  path('<int:pk>/edit', views.CourseUpdateView.as_view(),
        name='course_edit'),
  path('<int:pk>/delete', views.CourseDeleteView.as_view(),
        name='course_delete'),
  path('mine/', views.ManageCourseListView.as_view(),
        name='manage_course_list'),
]