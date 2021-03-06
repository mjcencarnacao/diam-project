from django.contrib.auth.decorators import permission_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, Profile
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from home.models import Comments, GenderMovies
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
    comments = Comments.objects.filter(critic_id=user.id).order_by('-entry')
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments, 'myuser': user})


def get_profile_page(request, user_id):
    comments_context = Comments.objects.filter(critic_id=user_id).order_by('-entry')
    user_context = User.objects.get(pk=user_id)
    return render(request, 'profile.html', {'critic': user_context, 'comments': comments_context})


def user_is_not_regular_check(user):
    if user.is_premium_user is False and user.is_pro_user is False:
        return False
    else:
        return True


def get_watchlist_page(request, user_id):
    movies = Movie.objects.filter(watch_list=user_id)
    gender_set = set()
    for movie in movies:
        genders = movie.gender.all()
        for g in genders:
            gender_set.add(g.gender)
    if request.method == 'POST':
        if request.POST['order'] == 'alphabet':
            movies = Movie.objects.filter(watch_list=user_id).order_by("name")
            return render(request, 'watchlist.html', {'movies': movies, 'genres': gender_set})
        if request.POST['order'] == 'year':
            movies = Movie.objects.filter(watch_list=user_id).order_by("raw__year")
            return render(request, 'watchlist.html', {'movies': movies, 'genres': gender_set})
        if request.POST['order']:
            res: str = request.POST.get('order')
            if res.isdigit():
                movies = Movie.objects.filter(watch_list=user_id)
                movie_to_erase = get_object_or_404(Movie, id=res)
                movie_to_erase.watch_list.remove(request.user)
                return render(request, 'watchlist.html', {'movies': movies, 'genres': gender_set})
            else:
                gender = GenderMovies.objects.get(gender=res)
                movies = Movie.objects.filter(watch_list=user_id, gender=gender.id)
                return render(request, 'watchlist.html', {'movies': movies, 'genres': gender_set})
    return render(request, 'watchlist.html', {'movies': movies, 'genres': gender_set})


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
    user = User.objects.get(pk=request.user.id)
    user.is_premium_user = False
    user.is_pro_user = False
    user.save()
    comments = Comments.objects.filter(critic_id=user.id).order_by('-entry')
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments, 'myuser': user})


def set_premium(request):
    user = User.objects.get(pk=request.user.id)
    user.is_premium_user = True
    user.is_pro_user = False
    user.save()
    comments = Comments.objects.filter(critic_id=user.id).order_by('-entry')
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments, 'myuser': user})


def set_pro(request):
    user: User = User.objects.get(pk=request.user.id)
    user.is_premium_user = False
    user.is_pro_user = True
    user.save()
    comments = Comments.objects.filter(critic_id=user.id).order_by('-entry')
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'form': form, 'comments': comments, 'myuser': user})
