""" sic_range_generator.py """
import scipy.stats
from ... import metrics as fr_metrics
from ...libs.data_access import SicRawDataAccess


class SicRangeGenerator:
    """ Gets a SIC Range, drawing samples from a pre-defined distribution """

    current = 0
    samples = []

    @fr_metrics.timeit
    def __init__(self, random_state):

        codes = parse_file()

        # setup a normal distribution function to create samples
        lower, upper = 0, len(codes)
        mu, sigma = 0, upper

        normal = scipy.stats.truncnorm(
            (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
        indices = normal.rvs(100000, random_state)

        for index in indices:
            idx = int(index)
            sic_range = codes[idx]
            self.samples.append(sic_range)

    @fr_metrics.timeit
    def make(self):
        """ Get a sample """
        if self.current > len(self.samples):
            self.current = 0

        value = self.samples[self.current]
        self.current += 1
        return value


def parse_file():
    """ get the sic raw data ranges """
    return SicRawDataAccess().get_sic_ranges()
