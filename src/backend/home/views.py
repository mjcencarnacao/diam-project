from typing import Dict

from django.shortcuts import render
from services import views
import json
from .models import Movie, Comments
from services.scrapper import Scrapper


# Create your views here. Request -> Response

def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie_comments_path = f"https://www.imdb.com{movie.raw['imdb_url']}reviews/?ref_=tt_ql_urv"
    try:
        check = Comments.objects.get(movie=movie.id)
    except Comments.DoesNotExist:
        # Podemos vir a ter um problema aqui caso sejamos nós a adicionar um filme ( solução pode passar por um boolean)
        comments_dictionary: Dict = Scrapper.get_movie_comments(movie_comments_path)
        for keys, value in comments_dictionary.items():
            Comments(tittle=keys, comment=value, movie=movie, critic=request.user).save()

    comments = Comments.objects.filter(movie=movie)
    return render(request, 'show_details.html', {'movie': movie, 'comments': comments})


def get_home_page(request):
    movies_source = json.loads(views.request_top_movies(request).content)
    print(movies_source[0]['name'])
    for movie in movies_source:
        try:
            movie_info = Movie.objects.get(name=movie['name'])
        except Movie.DoesNotExist:
            Movie(name=movie['name'], raw=movie).save()
            print("sucesso")

    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})


def get_login_page(request):
    return render(request, 'login.html')


def get_register_page(request):
    return render(request, 'register.html')
