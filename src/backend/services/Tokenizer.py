import re

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import HashingVectorizer


class Tokenizer:
    def __init__(self, stop_words: str = 'english'):
        self._stop_words = stop_words
        self._stop = stopwords.words(stop_words)

    @property
    def stop_words(self):
        return self._stop_words

    @property
    def stop_words_list(self):
        return self._stop

    @stop_words.setter
    def stop_words(self, value):
        self._stop_words = value
        self._stop = stopwords.words(self._stop_words)

    @staticmethod
    def tokenize(text: str) -> [str]:
        return text.split()

    @staticmethod
    def tokenize_porter(text: str) -> [str]:
        """
        :param text:
        :return: a vector with a text splited in words. This words are converted to their root form
        by Porter stemmer algorithm
        An alternative to Porter algorithm is the Snowball stemmer and Lancaster stemmer
        """
        porter = PorterStemmer()
        return [porter.stem(word) for word in text.split()]

    def tokenize_porter_with_stop_word(self, text: str) -> [str]:
        """
        :param text:
        :return:
        """
        porter_steam: [str] = Tokenizer.tokenize_porter(text)
        word_stop_steam = [w for w in porter_steam if w not in self._stop]
        return word_stop_steam

    def preprocessor(self, text: str) -> [str]:
        """
        :param text:
        :return:
        """
        """
            this method will find all HTML markups and remove them.
            This is not the best practice. To work with HTML markups
            we can use an sophisticated tool https://docs.python.org/3/library/html.parser.html
            after remove HTML the method replace all special characters to " " and join emoticons in the end
        """
        text: str = re.sub('<[^>]*>', '', text)
        emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)

        text: str = (re.sub('[\W]+', ' ', text.lower()) +
                     ' '.join(emoticons).replace('-', ''))

        tokenizer_word = self.tokenize_porter_with_stop_word(text=text)

        return tokenizer_word

    def hashing_vectorizer(self):
        return HashingVectorizer(decode_error='ignore',
                                 n_features=2 ** 21,
                                 preprocessor=None,
                                 tokenizer=self.preprocessor)
