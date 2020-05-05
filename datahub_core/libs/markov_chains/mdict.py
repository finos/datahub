""" MDict """
import numpy


class MDict:
    """ Markov dictionary """
    data: {}
    random_state: numpy.random.RandomState

    def __init__(self, random_state):
        self.data = {}
        self.random_state = random_state

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]

        raise KeyError(key)

    def add_key(self, prefix, suffix):
        """ add key """
        if prefix in self.data:
            self.data[prefix].append(suffix)
        else:
            self.data[prefix] = [suffix]

    def get_suffix(self, prefix):
        """ get suffix """
        suffix = self[prefix]
        return self.random_state.choice(suffix)
