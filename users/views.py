from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.



def subjects_and_their_courses(request):
    data={}
    courses= Courses.object.all()
    subjects = Subjects.objects.all()
    for sub in subjects:
        data[sub] = [c for c in courses if c.subject==sub]
    return JsonResponse(data)

    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST or None, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, ('your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(
                request, ('There was an error updating your profile'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'u_form': user_form, 'p_form': profile_form})    
