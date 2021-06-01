from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticatedUser, allowedUsers
# Create your views here.

def index(request):
    return render(request,'main/index.html',context={})

@unauthenticatedUser
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password.')
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    #returns the login page
    context = {'form':form}
    return render(request,'main/login.html',context)

def signupView(request):
    return render(request,'main/signup.html',context={})


def postRequest(request):
    return render(request,"main/landRequest.html",context={})