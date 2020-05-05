""" country data loader """
import csv
from ... import resource
from ...datasets import Country

COUNTRIES = []

def populate():
    raw = list(csv.reader(open(resource('country-codes.txt')), delimiter='\t'))
    count = 0
    for row in raw:
        name = row[0]
        alpha2 = row[1]
        alpha3 = row[2]
        locale = row[3]
        currency = row[4]
        region = row[5]

        country = Country(name, alpha2, alpha3, locale, currency, region, count)
        COUNTRIES.append(country)
        count += 1

populate()

class CountryDataAccess:
    """ Access to country data """

    countries = []

    def __init__(self):
        self.countries = COUNTRIES

    def get(self, region=None):
        """ Get a list of all countries"""
        if not region:
            return self.countries

        return list(filter(lambda x: x.region == region, self.countries))
