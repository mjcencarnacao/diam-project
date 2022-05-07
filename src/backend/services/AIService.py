import pickle
import os
import numpy as np
from .Tokenizer import Tokenizer

cur_dir = os.path.dirname(__file__)


class AIService(object):

    def __init__(self):
        t: Tokenizer = Tokenizer()
        self.vect = t.hashing_vectorizer()
        self.clf = pickle.load(open(os.path.join(cur_dir, 'AISerialized', 'pkl_objects', 'classifier.pkl'), 'rb'))

    def classify(self, document):
        label = {0: 'negative', 1: 'positive'}
        X = self.vect.transform([document])
        y = self.clf.predict(X)[0]
        print(self.clf.predict_proba(X))
        lst = self.clf.predict_proba(X)[0]
        return y, lst[0], lst[1]

    def train(self, document, y):
        X = self.vect.transform([document])
        self.clf.partial_fit(X, [y])
