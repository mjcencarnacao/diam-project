from django.template.defaulttags import register
from .models import Comments, Movie


@register.filter
def get_movie_likes(movie: Movie):
    return movie.likes.count()


@register.simple_tag
def count_movie_comments(movie_id, user_id):
    comments_counter: int = Comments.objects.filter(movie_id=movie_id, critic_id=user_id).count()
    return comments_counter


@register.simple_tag
def next_tag(lista, arg1):
    print("comment_id - " + str(arg1) + " nota - " + str(lista[lista.index(arg1) + 1]))
    return lista[lista.index(arg1) + 1]


@register.filter
def get_movie_name(dictionary):
    return dictionary.get('name')


@register.filter
def get_movie_cover(dictionary):
    return dictionary.get('image_url')


@register.filter
def get_movie_year(dictionary):
    return dictionary.get('year')


@register.filter
def get_movie_description(dictionary):
    return dictionary.get('desc')


@register.filter
def get_movie_genre(dictionary):
    genre = dictionary.get('genre')
    return str(genre).translate({ord(c): None for c in '[]\''})


@register.filter
def get_movie_actors(dictionary):
    genre = dictionary.get('actors')
    return str(genre).translate({ord(c): None for c in '[]\''})
