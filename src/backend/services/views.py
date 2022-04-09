from django.shortcuts import render
from django.http import JsonResponse
from . import scrapper

# Create your views here. Request -> Response


def request_top_movies(request):
    return JsonResponse(scrapper.Scrapper.get_movie_top(), safe=False)
