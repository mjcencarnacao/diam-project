from django.template.defaulttags import register


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
