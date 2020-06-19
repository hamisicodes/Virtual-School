from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Subject(models.Model):

    
    title = models.CharField(max_length =160,null = True)
    slug = models.SlugField(max_length=40)
    username= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('subjects-list')


class Course(models.Model):

    
    course_title = models.CharField(max_length =160,null = True)
    course_slug = models.SlugField(max_length=40)
    overview = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    username= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    subjects= models.ForeignKey(Subject,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.course_title  

    def get_absolute_url(self):
        return reverse ('subjects-list')

 

    