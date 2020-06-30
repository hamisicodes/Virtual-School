from django.db import models
from django.conf import settings
from content_management_system.models import Course

# Create your models here.

class Quiz(models.Model):
        course = models.ForeignKey(Course,on_delete=models.CASCADE)
        description = models.CharField(max_length = 70)
        roll_out= models.BooleanField(default=False)
        timestamp = models.DateTimeField(auto_now_add=True)
        name = models.CharField(max_length=100)
        
        class Meta:
            ordering = ['timestamp',]
            verbose_name_plural = "Quizzes"

        def __str__(self):
            return self.name


class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)

	def __str__(self):
		return self.label


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.label

class QuizTaker(models.Model):
	quiz_taker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	date_finished = models.DateTimeField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.email

    


class UsersAnswer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.question.label


