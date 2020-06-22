from django.db import models
# from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Subject(models.Model):

    title = models.CharField(max_length =160,null = True)
    slug = models.SlugField(max_length=40)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('subjects-list')

    @classmethod
    def search_by_title(cls,search_term):
        titles = cls.objects.filter(title__icontains=search_term)
        return titles


class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject =models.ForeignKey(Subject, on_delete=models.CASCADE,default=1)
    overview =models.TextField(max_length=300,default=1)
    students = models.ManyToManyField(User, related_name='students_to_course')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('-created',)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse('manage_courses_list')


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

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
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ContentBase(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_related')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def render(self):
        return render_to_string('courses/content/{}.html'.format(self._meta.model_name), {'item': self})

    def __str__(self):
        return self.title

class Text(ContentBase):
    content = models.TextField()

class File(ContentBase):
    file = models.FileField(upload_to='files')

class Image(ContentBase):
    file = models.FileField(upload_to='images')

class Video(ContentBase):
    url = models.URLField()
