
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns=[

    path('', views.index, name='index'),
    # path(r'^about/',views.about,name='about'),
    # path(r'^contact/',views.contact,name='contact'),

]



##register the MEDIA_ROOT route inorder to serve uploaded images on the development server
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)