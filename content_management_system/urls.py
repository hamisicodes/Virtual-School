from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import CreateSubject,SubjectView,SubjectDelete,UpdateSubject
from . import views


urlpatterns = [ 
path('new/subject', CreateSubject.as_view(template_name = 'content_management/create_subject.html'), name = 'create-subject'),
path('', SubjectView.as_view(template_name = 'content_management/subject.html'), name = 'subjects-list'),
path('subject/<int:pk>/update', UpdateSubject.as_view(template_name = 'content_management/subject_update.html'), name = 'subject-update'),
path('subject/<int:pk>/delete',SubjectDelete.as_view(), name = 'subject-delete'),
]