from django.urls import path,include
from . import views


urlpatterns = [
    
    path('question', views.create_question, name='create_question'),
    path('question/<int:pk>',views.create_answer, name ='create_answer'),


]
