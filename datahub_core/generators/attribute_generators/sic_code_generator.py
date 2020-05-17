""" sic_code_generator.py """
from ... import metrics as fr_metrics
from ...libs.data_access import SicRawDataAccess


class SicCodeGenerator:
    """ Generates SIC codes, drawing samples from a pre-defined distribution """

    codes = []

    @fr_metrics.timeit
    def __init__(self, random_state):
        self.codes = SicRawDataAccess().get_sic_data()
        self.random_state = random_state

    @fr_metrics.timeit
    def make(self, start, end):
        """ Get a sample """
        sample_set = []
        for code in self.codes:
            if start <= code.code <= end:
                sample_set.append(code)

        data = self.random_state.choice(sample_set)
        return data
