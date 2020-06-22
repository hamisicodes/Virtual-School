
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views


from .views import  contact_us



urlpatterns=[

    path('', views.index, name='index'),
    path(r'^contact/',views.contact_us, name='contact'),


]

