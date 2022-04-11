import json
import requests
from home import models


class Scrapper:

    @staticmethod
    def get_movie_top(url='https://raw.githubusercontent.com/theapache64/top250/master/top250_min.json'):
        request = json.loads(requests.get(url).text)
        # [models.Movie.objects.create(raw = movie).save() for movie in request]
        return request
