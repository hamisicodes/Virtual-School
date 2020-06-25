from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#from verified_email_field.forms import VerifiedEmailField

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]



#class UserSignUpForm(UserCreationForm):
    #email = forms.EmailField(max_length=100, help_text='Required')
    #class Meta:
        #model = User
        #fields = ('username', 'email', 'password1', 'password2')
#class UserUpdateForm(forms.ModelForm):
    
    #email = forms.EmailField()

    #class Meta:
        #model = User
        #fields = ['username', 'email']
#class ProfileForm(forms.ModelForm):

    #class Meta:
       # model = User
        #fields = [
            #sername',
            #'first_name', 
            #'last_name', 
            #'email',
            #]

#class ProfileUpdateForm(forms.ModelForm):
    #class Meta:
        #model = Profile
        #fields = ['image','bio','contacts']
       