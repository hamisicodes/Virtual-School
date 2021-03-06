from django.shortcuts import render, redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Question,Answer,Quiz,QuizTaker
from content_management_system.models import Course
from .forms import QuizCreateForm
from django.views.generic.edit import FormView
from .forms import MyForm
# Create your views here.

def list_of_quiz(request,pk):
    # course = Course.objects.all(course=pk)
    quizs = Quiz.objects.filter(course=pk)
    questions = Question.objects.all()
    answers = Answer.objects.all()
   
    # subject_courses = Course.objects.filter(subject=subject)
    context = {
        "quizs":quizs,
        "answers":answers,
        "questions":questions,
    }
    return render(request, 'online_test/quiz.html', context)

def create_quiz(request):
    quizs = Quiz.objects.all()
    form = QuizCreateForm()
    if request.method == 'POST':
        form = QuizCreateForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('create_question', quiz.pk)
    else:
        form = QuizCreateForm()
    context = {
        'form':form,
        'quizs':quizs
    }

    return render(request,'online_test/create_quiz.html',context)
def update_quiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    form = QuizCreateForm(instance=quiz)

    if request.method == 'POST':
        form = QuizCreateForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('quiz_create') 
    else:
        form = QuizCreateForm()
    return render(request, 'online_test/create_quiz.html', {'form':form,'quiz':quiz})


def create_question(request,pk):
    quiz = Quiz.objects.get(pk = pk)
    if request.method == 'POST' and request.POST.get('question'):
        question_label = request.POST.get('question')
        new_question = Question.objects.create(label = question_label, quiz=quiz)
        return redirect('create_question', quiz.pk)

    else:
        all_questions = Question.objects.filter(quiz=quiz)
        context ={
            'all_questions':all_questions,
            'quiz':quiz
        }

    return render(request ,'online_test/questions.html',context )

def create_answer(request, pk):

    try:
        question = Question.objects.get(pk= pk)
    
    except Question.DoesNotExist:
        return HttpResponse(status=404)
   
    if request.method == 'POST' and request.POST.get('answer'):
        answer_label = request.POST.get('answer')
        if request.POST.get('choices'):
            new_answer = Answer.objects.create(label = answer_label, question = question , is_correct = True)
        else:
            new_answer = Answer.objects.create(label = answer_label, question = question)

        return redirect('create_question', question.quiz.id)

    else:
        return redirect('create_question',question.quiz.id)



def myview(request):
    score = 0
    if request.method == 'POST':
        form = MyForm(request.POST)

        if 'done' in request.POST:
            # print(request.POST['my_object'])
            student_answer = request.POST.get('choices')
            answer = Answer.objects.get(label = student_answer)
            if answer.is_correct:
                score = 100
                quiztaker = QuizTaker.objects.create(quiz_taker = request.user , score = score , completed = True , quiz = answer.question.quiz )
            else:
                score = 0
                quiztaker = QuizTaker.objects.create(quiz_taker = request.user , score = score , completed = True , quiz = answer.question.quiz  )
            return redirect('results')
                
    else:
        return redirect('list_of_quiz' , 1)

def results(request):
   
    quiz_details = QuizTaker.objects.filter(quiz_taker = request.user)

    context ={
        'quiz_details':quiz_details  #queryset
    }

    return render(request,'online_test/results.html', context)



