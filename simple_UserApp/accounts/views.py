
# from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# to let the user know and get inside the site with login method
# for checking the user existance with authnicate method
from django.contrib.auth import authenticate, login, logout

# look the modelbackend which will handle the user authenication
# from django.contrib.auth import backends
from .forms import LoginForm, SignUpForm
# Create your views here.

# login_required decorators
from django.contrib.auth.decorators import login_required
# for new user creation
from django.contrib.auth.models import User
# using decorators here

# getusermodel for custom usermodel
# from django.contrib.auth import getusermodel
# User = getusermodel


def login_view(request):
    if request.method == 'POST':
        # for confirmation of post data
        print(request.POST)
        form = LoginForm(request.POST)

        if form.is_valid():
            # if form is valid and user exists
            user = authenticate(
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            
            if user:
                login(request, user)
                print(" A user is found--->", user)
                # redirection after login
                return redirect('/accounts/profile/')
            
            else:
                print("auth credentials donot match!")
                #ok, and login form will pass
                print(form.cleaned_data)
                return render(request,'accounts/fail.html')

    elif request.method == 'GET':
        # if request.user.is_authenticated:
            # return redirect('/accounts/profile-view/')
            
        form = LoginForm()

    # for invalid case
    return render(request, 'accounts/login.html',
    {'form': form})



@login_required
def profile_view(request):
    if request.user.is_authenticated:
        # pass
        # print 
        print("I am authenicated!")
        if request.user.is_superuser:
            print("I am admin")
        else:
            print("I am Guest!")
    else:
        # we have put conditionals but
        # with decorators login_required
        # we can do this in more shortcuts way
        # no auth give error
        # pass
        print("---I am not authenicated!---")
        return HttpResponse("Invalid User")
        # return render(request, 'accounts/fail.html')

    return render(request, 'accounts/profile.html')


def fail_view(request):
    return render(request, 'accounts/fail.html')


def logout_view(request):
    # for thrwoing or removing the cookies from browser
    logout(request)
    return redirect('/accounts/login/')
    # return render (request, 'accounts/login.html')

from django.contrib.auth.models import User
# for new user sign up 

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("congrats form is validated")
            print(form.cleaned_data)

            user = User(
                # first_name = form.cleaned_data['first_name'],
                # last_name = form.cleaned_data['last_name'],
                # email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                

                )

            user.save()
            # let's make password hash
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')

    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'accounts/signup.html',{'form': form})


#Note: by default if user in the model is not active or is_active is set to false
# then we cannot login bocz model backend doesnot allow us to login

# but we have allowall user method which can override the default

@login_required
def guest_view(request):
    if request.user.is_authenticated:
        # pass
        # print 
        print("I am authenicated!")
    else:
        # we have put conditionals but
        # with decorators login_required
        # we can do this in more shortcuts way
        # no auth give error
        # pass
        print("---I am not authenicated!---")
        return HttpResponse("Invalid User")
        # return render(request, 'accounts/fail.html')

    return render(request, 'accounts/guest.html')