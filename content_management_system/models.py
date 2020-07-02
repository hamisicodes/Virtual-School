from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.text import slugify









class Subject(models.Model):

    title = models.CharField(max_length =160,null = True)
    slug = models.SlugField(max_length=160)
    username= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('subjects-list')

    @classmethod
    def search_by_title(cls,search_term):
        titles = cls.objects.filter(title__icontains=search_term)
        return titles

    @property
    def number_of_courses(self):
        return Course.objects.filter(subject=self).count()


class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject =models.ForeignKey(Subject, on_delete=models.CASCADE,default=1)
    overview =models.TextField(max_length=2000,default=1)
    students = models.ManyToManyField(User, related_name='students_to_course')
    
    students = models.ManyToManyField(User,related_name='courses_joined',blank=True)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse('manage_courses_list')

    @property
    def number_of_modules(self):
        return Module.objects.filter(course=self).count()


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'], null =True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
        'model__in':('text', 'video', 'image', 'file')
    })
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'] , null = True)

    class Meta:
        ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_related')
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    def render(self):
        return render_to_string(f'courses/content/{self._meta.model_name}.html',{'item': self})


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()