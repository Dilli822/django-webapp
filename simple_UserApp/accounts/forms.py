
from django import forms
from django.contrib.auth.models import User
from django.forms.fields import CharField, EmailField
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    # max_length is 150 from models
    username = forms.CharField(max_length=100)
    # max password lenth is 128
    # putting *** this in password
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    
    #form validations for existing user
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("Username is taken")
        
        return self.cleaned_data['username']

    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Your Passwords donot match")


