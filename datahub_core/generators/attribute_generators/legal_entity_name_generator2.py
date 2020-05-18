""" legal_entity_name_generator """
import json
import numpy
from ... import metrics
from ... import resource
from .company_name_markov import CompanyNameMarkov
from .company_name_suffix import CompanyNameSuffixGenerator

NAMES = []
SIC = {}
DATA = json.loads(open(resource('sic-conventions.json')).read())

CLIENT_TYPES = {}

for item in DATA:
    sic_code = item['code']
    SIC[sic_code] = item

for item in DATA:
    for ct in item['client_type']:
        if ct not in CLIENT_TYPES.keys():
            CLIENT_TYPES[ct] = []
        CLIENT_TYPES[ct].append(item)

SUFFIC_GENERATOR = CompanyNameSuffixGenerator()


class LegalEntityNameGenerator2:
    """ Generates legal entity names using Markov-Chains """

    random_state: numpy.random.RandomState
    sic = {}

    def __init__(self, randomstate):
        self.random_state = randomstate
        self.namer = CompanyNameMarkov(self.random_state)

    @metrics.timeit
    def make(self, sic, country_code=None):
        """ Make a name """
        config = SIC[sic.code]
        return self.create_name(config, country_code)

    @metrics.timeit
    def make_clienttype(self, client_type, country_code=None):
        """ Make a name """
        client_types = CLIENT_TYPES[client_type]
        config = self.random_state.choice(client_types)
        return self.create_name(config, country_code)

    @metrics.timeit
    def create_name(self, config, country_code):
        while True:
            model = config['models'][0]

            full_name = self.namer.make(model)

            postfixes = config['postfixes']

            for group in postfixes:
                choice = self.random_state.choice(group)
                if len(choice) > 1:
                    full_name = full_name.strip()
                    full_name = full_name + " " + self.random_state.choice(group)

            v = full_name.strip()
            if v not in NAMES:
                NAMES.append(v)

                if country_code:
                    suffix = SUFFIC_GENERATOR.make(country_code)
                    return f"{v} {suffix}"
                return v
