""" company name generator using faker """
import numpy
from faker import Faker
from faker.providers import company
from ... import metrics as fr_metrics


class CompanyNameFaker:
    """ Generates company name using Markov-Chains """

    random_state: numpy.random.RandomState

    @fr_metrics.timeit
    def __init__(self, seed):
        self.seed = seed

    @fr_metrics.timeit
    def make(self, country):
        """ Make a name """
        fake = Faker(country.locale)
        fake.seed_instance(self.seed)
        fake.add_provider(company)

        return fake.format('company')
