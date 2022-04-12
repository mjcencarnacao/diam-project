import json
import requests
from bs4 import BeautifulSoup

class Scrapper:

    @staticmethod
    def get_movie_top(url='https://raw.githubusercontent.com/theapache64/top250/master/top250_min.json'):
        request = json.loads(requests.get(url).text)
        return request

    @staticmethod
    def get_movie_comments(url:str) -> dict:
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        titles = [a.text for a in soup.select('a.title')]
        descriptions = [a.text for a in soup.select('div.text')]
        return dict(zip(titles, descriptions))