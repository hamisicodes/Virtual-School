 from django.urls import path,include
from . import views


urlpatterns = [
    
    path('<int:pk>/question', views.create_question, name='create_question'),
    path('question/<int:pk>',views.create_answer, name ='create_answer'),
    path('list_of_quiz/(<int:pk>)/', views.list_of_quiz, name='list_of_quiz'),
    path('create_quiz/', views.create_quiz, name='quiz_create'),
    path('update_quiz/(<int:pk>)/', views.update_quiz, name='quiz_update'),
    path('post_quiz/',views.myview , name = 'post_quiz'),
    path('results/',views.results , name = 'results'),


]