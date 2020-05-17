""" legal_entity_generator module """
from faker import Faker
from faker.providers import address
from ...datasets import Address
from ... import metrics as fr_metrics

FAKERS = {}

class AddressGenerator:
    """ Generates addresses for a specific country, the addresses are not real """

    seed: int
    addresses = {}

    @fr_metrics.timeit
    def __init__(self, randomstate):
        self.randomstate = randomstate

    @fr_metrics.timeit
    def make(self, country):
        """ Make an address """

        if country.locale not in FAKERS:
            fake = Faker(country.locale)
            fake.add_provider(address)
            FAKERS[country.locale] = fake

        fake = FAKERS[country.locale]
        seed = self.randomstate.rand(1)[0]
        fake.seed_instance(seed)

        state = get_state_function(fake)

        return Address(
            fake.format('building_number'),
            fake.format('street_name'),
            fake.format('city'),
            state,
            "")

@fr_metrics.timeit
def get_state_function(faker):
    """ Fakers state function changes depending on the locale """

    if has_function(faker, 'state'):
        return faker.format('state')
    if has_function(faker, 'province'):
        return faker.province()
    if has_function(faker, 'county'):
        return faker.county()
    if has_function(faker, 'prefecture'):
        return faker.prefecture()
    if has_function(faker, 'region'):
        return faker.region()

    return ""

@fr_metrics.timeit
def has_function(faker, key):
    """ helper function to check if a method is available on an object"""
    return hasattr(faker, key)
