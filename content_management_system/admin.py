from django.contrib import admin
from .models import Subject,Course, Module, Content, ContentBase

# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Content)
# admin.site.register(ContentBase)