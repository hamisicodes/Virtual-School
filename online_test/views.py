from django.shortcuts import render
from .models import Quiz

# Create your views here.
def list_of_quiz(request):
    quizs = Quiz.objects.all()
    context = {
        "quizs":quizs
    }
    return render(request, 'online_test/quiz.html', context)