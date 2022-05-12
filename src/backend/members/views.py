from xml.etree.ElementTree import Comment

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, Profile
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from home.models import Comments
from django.shortcuts import get_object_or_404
from .models import User
from home.models import Movie


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


def login_user_profile(request):
    user = request.user
    comments = Comments.objects.filter(critic_id=user.id)
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES,  instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments})


def get_profile_page(request, user_id):
    comments_context = Comments.objects.filter(critic_id=user_id)
    user_context = User.objects.get(pk=user_id)
    return render(request, 'profile.html', {'critic': user_context, 'comments': comments_context})

def get_watchlist_page(request, user_id):
    movies = Movie.objects.filter(watchlist=user_id)
    return render(request, 'watchlist.html', {'movies': movies})


def logout_user(request):
    logout(request)
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


def set_regular(request):
    user = request.user
    comments = Comments.objects.filter(critic_id=user.id)
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES,  instance=user)
        if form.is_valid():
            form.save()  
    cur_user = User.objects.get(pk=request.user.id)
    cur_user.is_premium_user = False
    cur_user.is_pro_user = False
    cur_user.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments})


def set_premium(request):
    user = request.user
    comments = Comments.objects.filter(critic_id=user.id)
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES,  instance=user)
        if form.is_valid():
            form.save()
    cur_user = User.objects.get(pk=request.user.id)
    cur_user.is_premium_user = True
    cur_user.is_pro_user = False
    cur_user.save()
    user_context = User.objects.get(pk=request.user.id)
    return render(request, 'user_profile.html', {'form': form, 'comments': comments})

def set_pro(request):
    user = request.user
    comments = Comments.objects.filter(critic_id=user.id)
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES,  instance=user)
        if form.is_valid():
            form.save()
    #comments_context = Comments.objects.filter(critic_id=request.user.id)
    cur_user: User = User.objects.get(pk=request.user.id)
    cur_user.is_premium_user = False
    cur_user.is_pro_user = True
    cur_user.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments})
