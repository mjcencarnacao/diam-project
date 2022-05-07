from collections import defaultdict
from typing import Dict


class DictionaryManager:
    old = ["Title", "Year", "imdbID", "Poster"]
    new = ["name", "year", "imdb_url", "image_url"]

    @staticmethod
    def __change_key(d: Dict, lst_new_keys: [str], lst_old_keys: [str]) -> None:
        for (i, j) in zip(lst_new_keys, lst_old_keys):
            d[i] = d.pop(j)

    @staticmethod
    def change_keys_in_dictionary_list(lst: [Dict],
                                       lst_new_keys: [str] = new,
                                       lst_old_keys: [str] = old) -> [Dict]:
        for d in lst:
            DictionaryManager.__change_key(d, lst_new_keys, lst_old_keys)
        return lst

    @staticmethod
    def merge_two_dictionaries(lst1: [Dict], lst2: [Dict]) -> [Dict]:
        d = defaultdict(dict)
        for item in lst1 + lst2:
            d[item["name"]].update(item)
        return list(d.values())

