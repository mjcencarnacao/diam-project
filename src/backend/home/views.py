from django.shortcuts import render
from services import views
import json
from .models import  Movie

# Create your views here. Request -> Response


def get_home_page(request):

    movies = json.loads(views.request_top_movies(request).content)
    print(movies[0]['name'])
    for movie in movies:
        try:
            movie_info = Movie.objects.get(name=movie['name'])
        except Movie.DoesNotExist:
            Movie(name=movie['name'],raw= movie).save()
            print("sucesso")
    return render(request, 'index.html', {'movies': movies})


def get_login_page(request):
    return render(request, 'login.html')


def get_register_page(request):
    return render(request, 'register.html')
    
