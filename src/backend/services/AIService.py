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
        proba = np.max(self.clf.predict_proba(X))
        return y, proba

    def train(self, document, y):
        X = self.vect.transform([document])
        self.clf.partial_fit(X, [y])
