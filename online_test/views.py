from django.shortcuts import render
from .models import Quiz
from content_management_system.models import Course

# Create your views here.
def list_of_quiz(request,pk):
    # course = Course.objects.all(course=pk)
    quizs = Quiz.objects.filter(course=pk)
    # subject_courses = Course.objects.filter(subject=subject)
    context = {
        "quizs":quizs
    }
    return render(request, 'online_test/quiz.html', context)