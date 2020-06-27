from django.urls import path
from . import views

urlpatterns = [
    path('list_of_quiz/(<int:pk>)/', views.list_of_quiz, name='list_of_quiz')
]