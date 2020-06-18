from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def student_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid()
            form.save(0)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Student Account created for {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'student/register.html',{'form':form})