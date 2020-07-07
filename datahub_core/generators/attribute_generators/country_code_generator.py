""" country_code_generator module """
from datahub_core.generators.attribute_generators.sic_range_generator import ChoiceGenerator
from datahub_core import metrics as fr_metrics
from datahub_core.data import data_access

class CountryCodeGenerator:
    """ CountryCodeGenerator Allows sampling of country-codes based on a normal distribution """
    countries = []
    samples = []
    current = 0

    @fr_metrics.timeit
    def __init__(self, random_state, region=None, sampler=ChoiceGenerator):
        data = data_access.countries(region=region)
        self.sampler = sampler(random_state, data=data)

    @fr_metrics.timeit
    def make(self):
        return self.sampler.make()
