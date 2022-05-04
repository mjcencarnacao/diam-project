from typing import Dict

from django.shortcuts import render
from django.http import HttpResponseRedirect
from services import views
import json
from .models import Movie, Comments
from services.scrapper import Scrapper
from services.AIService import AIService
from members.forms import SignUpForm


def movie_details(request, movie_id):
    ai_service: AIService = AIService()
    movie = Movie.objects.get(pk=movie_id)
    movie_comments_path = f"https://www.imdb.com{movie.raw['imdb_url']}reviews/?ref_=tt_ql_urv"

    check = Comments.objects.filter(movie=movie.id)
    if not check:
        # Podemos vir a ter um problema aqui caso sejamos nós a adicionar um filme ( solução pode passar por um boolean)
        comments_dictionary: Dict = Scrapper.get_movie_comments(movie_comments_path)
        for keys, value in comments_dictionary.items():
            ai_feedback, ai_prob = ai_service.classify(value)
            Comments(title=keys,
                     comment=value,
                     movie=movie,
                     critic=request.user,
                     Ai_FeedBack=ai_feedback,
                     Ai_Probability_FeedBack=ai_prob).save()

    comments = Comments.objects.filter(movie=movie)
    return render(request, 'details.html', {'movie': movie, 'comments': comments})


def get_home_page(request):
    movies_source = json.loads(views.request_top_movies(request).content)
    print(movies_source[0]['name'])
    for movie in movies_source:
        try:
            movie_info = Movie.objects.get(name=movie['name'])
        except Movie.DoesNotExist:
            Movie(name=movie['name'], raw=movie).save()

    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})


def get_register_page(request):
    submitted = False
    if request.method == 'POST':
        form = SignUpForm(request.POT)
        if form.is_valid():
            form.save()
            movies = Movie.objects.all()
            return HttpResponseRedirect('login.html')
    else:
        form = SignUpForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register.html', {'form': form, 'submitted': submitted})


def user_comment(request):
    return render(request, 'details.html')

