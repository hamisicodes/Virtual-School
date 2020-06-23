from django.contrib import admin
from .models import Subject,Course,Module
from django.utils.translation import gettext_lazy as _
# Register your models here.
<<<<<<< HEAD
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Content)
# admin.site.register(ContentBase)
=======


class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('course_name',)}
    inlines = [ModuleInline]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
>>>>>>> 03744f46d84e0122ff9ff5b378a36c21614f1ba2
