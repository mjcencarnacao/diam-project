from django.shortcuts import render
from services import views
import json


# Create your views here. Request -> Response


def get_home_page(request):
    movies = json.loads(views.request_top_movies(request).content)
    return render(request, 'index.html', {'movies': movies})


def get_login_page(request):
    return render(request, 'login.html')


def get_register_page(request):
    return render(request, 'register.html')

def get_details_page(request):
    return render(request, 'details.html')
    
