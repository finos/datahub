from faker import Faker
from faker import providers
from ... import metrics as fr_metrics

FAKERS = {}

class PersonGenerator:
    """ Generates addresses for a specific country, the addresses are not real """

    seed: int
    addresses = {}

    @fr_metrics.timeit
    def __init__(self, randomstate):
        self.randomstate = randomstate

    @fr_metrics.timeit
    def make(self, country):

        if country.locale not in FAKERS:
            fake = Faker(country.locale)
            fake.add_provider(providers.person)
            FAKERS[country.locale] = fake

        fake = FAKERS[country.locale]
        seed = self.randomstate.rand(1)[0]
        fake.seed_instance(seed)

        return fake.format('name')
