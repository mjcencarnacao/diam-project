import pickle
import os
import numpy as np
from .Tokenizer import Tokenizer

cur_dir = os.path.dirname(__file__)

dest = os.path.join(cur_dir, 'AISerialized', 'pkl_objects', 'classifier.pkl')


class AIService(object):

    def __init__(self):
        self.label = {0: 'negative', 1: 'positive'}
        t: Tokenizer = Tokenizer()
        self.vect = t.hashing_vectorizer()
        self.clf = pickle.load(open(os.path.join(cur_dir, 'AISerialized', 'pkl_objects', 'classifier.pkl'), 'rb'))

    def classify(self, document):
        label = {0: 'negative', 1: 'positive'}
        X = self.vect.transform([document])
        y = self.clf.predict(X)[0]
        lst = self.clf.predict_proba(X)[0]
        return y, lst[0], lst[1]

    def train(self, document, y):
        X = self.vect.transform([document])
        self.clf.partial_fit(X, [y])

    def train_and_serialize(self, document, y):
        X = self.vect.transform([document])
        self.clf.partial_fit(X, [y])
        pickle.dump(self.clf,
                    open(dest, 'wb'), protocol=4)

    def get_comment_plaintext(self, ai_numeric_feedback):
        return self.label[ai_numeric_feedback]
