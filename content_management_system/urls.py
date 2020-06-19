from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import CreateSubject,SubjectView,SubjectDelete,UpdateSubject,SubjectDetail,CourseDelete,UpdateCourse
from . import views


urlpatterns = [ 
path('new/subject', CreateSubject.as_view(template_name = 'content_management/create_subject.html'), name = 'create-subject'),
path('', SubjectView.as_view(template_name = 'content_management/subject.html'), name = 'subjects-list'),
path('subject/<int:pk>/update', UpdateSubject.as_view(template_name = 'content_management/subject_update.html'), name = 'subject-update'),
path('subject/<int:pk>/delete',SubjectDelete.as_view(), name = 'subject-delete'),
path('course/<int:pk>/delete',CourseDelete.as_view(), name = 'course-delete'),
path('course/<int:pk>/update',UpdateCourse.as_view(template_name = 'content_management/course_update.html'), name = 'course-update'),
path('subject/<int:pk>/', SubjectDetail.as_view(), name = 'subject-detail'),
]