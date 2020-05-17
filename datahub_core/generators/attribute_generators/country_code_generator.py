""" country_code_generator module """
import scipy.stats
from ... import metrics as fr_metrics
from ...libs.data_access import CountryDataAccess


class CountryCodeGenerator:
    """ CountryCodeGenerator Allows sampling of country-codes based on a normal distribution """
    countries = []
    samples = []
    current = 0

    @fr_metrics.timeit
    def __init__(self, random_state):
        self.random_state = random_state

        self.countries = CountryDataAccess().get()

        # setup a normal distribution function to create samples
        lower, upper = 0, len(self.countries)
        m_u, sigma = 0, upper / 4

        normal_gen = scipy.stats.truncnorm(
            (lower - m_u) / sigma, (upper - m_u) / sigma,
            loc=m_u,
            scale=sigma)

        normal_gen.random_state = self.random_state
        indices = normal_gen.rvs(1000, random_state=self.random_state)

        for index in indices:
            country = self.countries[int(index)]
            self.samples.append(country)

    @fr_metrics.timeit
    def make(self):
        """ Sample a country code """
        if self.current >= len(self.samples):
            self.current = 0

        country = self.samples[self.current]

        self.current += 1
        return country
