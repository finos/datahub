""" sic_range_generator.py """
from datahub_core.data import data_access
from ... import metrics as fr_metrics
from . import ChoiceGenerator

class SicRangeGenerator:
    """ Gets a SIC Range, drawing samples from a pre-defined distribution """

    @fr_metrics.timeit
    def __init__(self, random_state, sampler=ChoiceGenerator):
        self.sampler = sampler(
            random_state=random_state,
            data=data_access.sic_ranges())

    @fr_metrics.timeit
    def make(self):
        return self.sampler.make()
