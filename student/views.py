from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt


from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this
from .forms import ContactForm # Add this
from django.core.mail import send_mail

# Create your views here.
def index(request):
    date =dt.date.today()
    return render(request, 'student/index.html', {"date":date })



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])



            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

