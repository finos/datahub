#pylint:disable=no-self-use
""" company name generator using faker """
from faker import Faker
from faker.providers import company
from ... import metrics as fr_metrics

FAKERS = {
}

class CompanyNameSuffixGenerator:
    """ Generates company name using Markov-Chains """

    @fr_metrics.timeit
    def make(self, country):
        """ Make a suffix """

        if country.locale not in FAKERS:
            fake = Faker(country.locale)
            fake.add_provider(company)
            FAKERS[country.locale] = fake

        fake = FAKERS[country.locale]

        while True:
            ## We didn't like 'and sons'
            value = fake.format('company_suffix')
            if value != 'and Sons':
                return value
