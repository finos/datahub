""" lei_generator """
import numpy
from ... import metrics as fr_metrics
from ...datasets import LEI


class LeiGenerator: # pylint: disable=too-few-public-methods
    """ Generates Lei numbers """

    @fr_metrics.timeit
    def __init__(self, random_state):
        self.random_state = random_state

    @fr_metrics.timeit
    def make(self):
        """ MARKE an LEI CODE """
        lou_code = self.random_state.randint(1000, 9999)
        identifier = self.random_state.randint(100000000000, 999999999999, dtype=numpy.int64)

        return LEI(str(lou_code), str(identifier)).get()
