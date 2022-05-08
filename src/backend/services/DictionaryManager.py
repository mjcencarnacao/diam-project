from collections import defaultdict
from typing import Dict
from .scrapper import Scrapper


class DictionaryManager:
    old = ["Title", "Year", "imdbID", "Poster", "Plot", "Actors", "Genre"]
    new = ["name", "year", "imdb_url", "image_url", "desc", "actors", "genre"]

    @staticmethod
    def __change_key(d: Dict) -> Dict:
        for (i, j) in zip(DictionaryManager.new, DictionaryManager.old):
            d[i] = d.pop(j)
        return d

    @staticmethod
    def change_keys_in_dictionary_list(lst: [Dict]) -> [Dict]:
        correct_list = [d for d in lst if all(k in d.keys() for k in DictionaryManager.old)]
        return list(map(DictionaryManager.__change_key, correct_list))

    @staticmethod
    def set_fix_imdb_url(lst: [Dict]) -> None:
        for d in lst:
            d["imdb_url"] = f'/title/{d["imdb_url"]}/'
            DictionaryManager.set_Genre_and_Actor_to_correct_format(d)

    @staticmethod
    def get_all_information(lst: [Dict]) -> [Dict]:
        lst_of_all_info = []
        for d in lst:
            movie_all_info = Scrapper.get_all_movie_info(d['Title'])
            movie_all_info["imdb_url"] = d["imdbID"]
            lst_of_all_info.append(movie_all_info)
        return lst_of_all_info

    @staticmethod
    def set_Genre_and_Actor_to_correct_format(dct: Dict) -> None:
        dct["genre"] = dct["genre"].split(',')
        dct["actors"] = dct["actors"].split(',')
