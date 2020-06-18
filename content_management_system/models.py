from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Subject(models.Model):

    
    title = models.CharField(max_length =160,null = True)
    slug = models.SlugField(max_length=40)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('subjects-list')
