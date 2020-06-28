from django.shortcuts import render, redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Question,Answer,Quiz
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

def create_question(request):
   
    if request.method == 'POST' and request.POST.get('question'):
        question_label = request.POST.get('question')
        new_question = Question.objects.create(label = question_label, quiz_id = 1)
        return redirect('create_question')

    else:
        all_questions = Question.objects.all()
        context ={
            'all_questions':all_questions
        }

    return render(request ,'online_test/questions.html',context )

def create_answer(request, pk):

    try:
        question = Question.objects.get(pk= pk)
    
    except Question.DoesNotExist:
        return HttpResponse(status=404)
   
    if request.method == 'POST' and request.POST.get('answer'):
        answer_label = request.POST.get('answer')
        new_answer = Answer.objects.create(label = answer_label, question = question)
        return redirect('create_question')

    else:
        return redirect('create_question')






