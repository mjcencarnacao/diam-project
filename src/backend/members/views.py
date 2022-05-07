from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .models import User



# Create your views here.
def register(request):
    msg = None

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('members:login_user')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_user(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')
            else:
                messages.success(request, "Invalid Credentials")
                return redirect('members:login_user')
    else:
        msg = 'error validation form'
        return render(request, 'authenticate/login.html', {'form': form})



def home(request):
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return render(request, 'authenticate/login.html')