from django.template.defaulttags import register


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
    return  str(genre).translate({ord(c): None for c in '[]\''})

@register.filter
def get_movie_actors(dictionary):
    genre = dictionary.get('actors')
    return  str(genre).translate({ord(c): None for c in '[]\''})
