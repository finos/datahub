#pylint:disable=no-self-use
""" lei_generator """
import re
from ... import resource
from ... import metrics as fr_metrics

@fr_metrics.timeit
def prep_file(file_name):
    items = []

    with open(file_name) as files:
        for newline in files:
            items.append(newline)
    return items

ASSET_CLASS = prep_file(resource('funds/asset_class.csv'))
DIVIDEND_TREATMENT = prep_file(resource('funds/dividend_treatment.csv'))
REGIONS = prep_file(resource('funds/regions.csv'))
CLASS = prep_file(resource('funds/classes.csv'))


class FundNameGenerator: # pylint: disable=too-few-public-methods
    """ Generates Lei numbers """

    @fr_metrics.timeit
    def __init__(self, random_state):
        self.random_state = random_state

    @fr_metrics.timeit
    def make(self, legal_entity):
        """ Make a new name for a fund """

        provider = self.get_fund_provider(legal_entity)
        region = self.get_geographic_region()
        asset = self.get_asset()
        asset_class = self.get_class()
        divi = self.get_dividend_type()

        return f'{provider} {region} {asset} {asset_class} {divi}'

    def get_geographic_region(self):
        """ Samples a geographic region for this fund, eg. G10, Emerging Markets"""
        return self.random_state.choice(REGIONS).strip()

    def get_fund_provider(self, legal_entity):
        """ Gets the name of the funded provider"""

        parts = re.split(r'\s+|[,;.-]\s*', legal_entity)

        if len(parts) > 1:
            return make_name_abbreviation(parts)

        return legal_entity.split(' ')[0].strip()

    def get_asset(self):
        """ Samples the assets class, e.g. Equities, Fixed Income"""
        return self.random_state.choice(ASSET_CLASS).strip()

    def get_class(self):
        """ The class of the assets, e.g. ClassA --> Junk"""
        return self.random_state.choice(CLASS).strip()

    def get_dividend_type(self):
        """ Samples the dividend type, e.g. accumlator,  """
        return self.random_state.choice(DIVIDEND_TREATMENT).strip()

def make_name_abbreviation(words):
    return ''.join([word[:1].upper() for word in words])
