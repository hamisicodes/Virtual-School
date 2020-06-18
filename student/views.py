from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
# Create your views here.
def index(request):
    date =dt.date.today()
    return render(request, 'student/index.html', {"date":date })

def about(request):
    date = dt.date.today()
    return render(request, 'student/about.html', {"date": date})



def contact(request):
    date = dt.date.today()
    return render(request, 'student/contact.html', {"date": date})
