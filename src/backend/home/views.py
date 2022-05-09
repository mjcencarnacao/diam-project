from typing import Dict

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from services import views
import json
from .models import Movie, Comments
from services.scrapper import Scrapper
from services.AIService import AIService
from members.forms import SignUpForm
from django.core.files.storage import FileSystemStorage
from members.models import User
from services.DictionaryManager import DictionaryManager
from services.ProcessingService import ProcessingService


def movie_details(request, movie_id):
    if request.method == 'POST':
        if 'filter_button_negative' in request.POST:
            movie_id = movie_id
            movie = Movie.objects.get(pk=movie_id)
            comments = Comments.objects.filter(movie=movie, Ai_FeedBack=0)
            return render(request,
                          'details.html',
                          {'movie': movie,
                           'comments': comments,
                           'positive_percentage': 0,})

        if 'filter_button_positive' in request.POST:
            movie_id = movie_id
            movie = Movie.objects.get(pk=movie_id)
            comments = Comments.objects.filter(movie=movie, Ai_FeedBack=1)
            return render(request,
                          'details.html',
                          {'movie': movie,
                           'comments': comments,
                           'positive_percentage': 100, })

        if 'filter_button_user' in request.POST:
            movie_id = movie_id
            movie = Movie.objects.get(pk=movie_id)
            critic_id: int = request.POST.get('filter_button_user')
            comments = Comments.objects.filter(movie=movie, critic_id=critic_id)
            positive_percentage = ProcessingService.positive_percentage(comments)
            return render(request,
                          'details.html',
                          {'movie': movie,
                           'comments': comments,
                           'positive_percentage': positive_percentage, })

        ai_service: AIService = AIService()
        comment_value = request.POST.get('comentario')
        ai_feedback, neg, pos = ai_service.classify(comment_value)
        movie = Movie.objects.get(pk=movie_id)
        Comments(title=request.POST.get('titulo'),
                 comment=comment_value,
                 movie=movie,
                 movie_name=movie.name,
                 critic=request.user,
                 critic_username=request.user.username,
                 Ai_FeedBack=ai_feedback,
                 Ai_Probability_PositiveFeedBack=pos,
                 Ai_Probability_NegativeFeedBack=neg).save()

    ai_service: AIService = AIService()
    movie = Movie.objects.get(pk=movie_id)
    movie_comments_path = f"https://www.imdb.com{movie.raw['imdb_url']}reviews/?ref_=tt_ql_urv"

    check = Comments.objects.filter(movie=movie.id)
    if not check:
        # Podemos vir a ter um problema aqui caso sejamos nós a adicionar um filme ( solução pode passar por um boolean)
        comments_dictionary: Dict = Scrapper.get_movie_comments(movie_comments_path)
        for keys, value in comments_dictionary.items():
            ai_feedback, neg, pos = ai_service.classify(value)
            Comments(title=keys,
                     comment=value,
                     movie=movie,
                     movie_name=movie.name,
                     critic_username='ImdbUser',
                     Ai_FeedBack=ai_feedback,
                     Ai_Probability_PositiveFeedBack=pos,
                     Ai_Probability_NegativeFeedBack=neg).save()

    comments = Comments.objects.filter(movie=movie)
    positive_percentage = ProcessingService.positive_percentage(comments)

    return render(request, 'details.html', {'movie': movie,
                                            'comments': comments,
                                            'positive_percentage': positive_percentage, })


def search_movies(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_movies = Scrapper.get_search_movies(searched)
        pre_movie_list = DictionaryManager.get_all_information(searched_movies)
        all_information_movies = DictionaryManager.change_keys_in_dictionary_list(pre_movie_list)
        DictionaryManager.set_fix_imdb_url(all_information_movies)
        for i in range(0, len(all_information_movies)):
            check = Movie.objects.filter(name=all_information_movies[i]['name'])
            if not check:
                Movie(name=all_information_movies[i]['name'], raw=all_information_movies[i]).save()

        db_movies = Movie.objects.filter(name__regex=rf'({searched})+')
        return render(request, 'searched_movies.html', {'movies': db_movies})
    else:
        return render(request, 'searched_movies.html',
                      {})


def get_home_page(request):
    movies_source = json.loads(views.request_top_movies(request).content)
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


def like(request):
    if request.method == 'POST':
        result = ''
        id: int = request.POST.get('postid')
        p_id: int = id
        post = get_object_or_404(Comments, id=id)
        post.likes += 1
        result = post.likes
        post.save()

    return JsonResponse({'result': result, 'p_id': p_id, })


def dislike(request):
    if request.method == 'POST':
        result = ''
        id: int = request.POST.get('postid')
        p_id: int = id
        post = get_object_or_404(Comments, id=id)
        if post.likes == 0:
            result = post.likes
            return JsonResponse({'result': result, 'p_id': p_id, })
        post.likes -= 1
        result = post.likes
        post.save()

    return JsonResponse({'result': result, 'p_id': p_id, })


def user_comment(request):
    return render(request, 'details.html')

def fazer_upload(request):
    if request.method == 'POST':
        myfile = request.POST.FILES('thefile', False)
        fs = FileSystemStorage()
        filename = fs.save(request.user.username, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'votacao/fazer_upload.html', {'uploaded_file_url': uploaded_file_url})

def get_profile_page(request, user_id):
    comments_context = Comments.objects.filter(critic_id=user_id)
    user_context = User.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user': user_context, 'comments': comments_context})


def get_eval(request):
    if request.method == 'POST':
        new_result = 'ya meu'
        id_and_oldresult: str = request.POST.get('postid')
        parts: list(str) = id_and_oldresult.split("-")
        p_id :str = parts[0]

    return JsonResponse({'result': new_result, 'p_id': p_id, })