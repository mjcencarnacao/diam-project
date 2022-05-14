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
            DictionaryManager.add_movie_info_to_list(lst_of_all_info, srapper_info=movie_all_info,dict=d)
        return lst_of_all_info

    @staticmethod
    def set_Genre_and_Actor_to_correct_format(dct: Dict) -> None:
        dct["genre"] = dct["genre"].split(',')
        dct["actors"] = dct["actors"].split(',')

    @staticmethod
    def add_movie_info_to_list(lst: [Dict],srapper_info: Dict, dict: Dict) -> None:
        if srapper_info["Plot"] != "N/A" and srapper_info["Poster"] != "N/A":
            srapper_info["imdb_url"] = dict["imdbID"]
            lst.append(srapper_info)

    @staticmethod
    def get_movie_genre(dictionary: Dict):
        genre = dictionary.get('genre')
        return str(genre).translate({ord(c): None for c in '[]\''})
