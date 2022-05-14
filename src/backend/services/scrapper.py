import json
from typing import Dict

import requests
from bs4 import BeautifulSoup


class Scrapper:

    @staticmethod
    def get_movie_top(url='https://raw.githubusercontent.com/theapache64/top250/master/top250_min.json') -> json:
        request = json.loads(requests.get(url).text)
        return request

    @staticmethod
    def get_movie_comments(url: str) -> dict:
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        titles = [a.text for a in soup.select('a.title')]
        descriptions = [a.text for a in soup.select('div.text')]
        return dict(zip(titles, descriptions))

    @staticmethod
    def get_search_movies(movie_name: str) -> [Dict]:
        url: str = f"https://www.omdbapi.com/?s={movie_name}&apikey=1bf54cb4"
        request = json.loads(requests.get(url).text)
        try:
            return request["Search"]
        except KeyError:
            return []

    @staticmethod
    def get_all_movie_info(movie_name: str):
        url: str = f"https://www.omdbapi.com/?t={movie_name}&apikey=1bf54cb4"
        request = json.loads(requests.get(url).text)
        return request
