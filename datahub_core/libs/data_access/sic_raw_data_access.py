#pylint:disable=no-self-use
""" sic_loader module """
import json
from ... import resource
from ...datasets import SicCode
from ...datasets import SicRange

SIC_RANGES = []
ROWS = open(resource('sic-ranges.txt')).read().split('\n')
for row in ROWS:
    parts = row.split('\t')
    code = SicRange(parts[0], parts[1], parts[2])
    SIC_RANGES.append(code)

## process the sic conventions
JSON_DATA = open(resource('sic-conventions.json')).read()
RAW = json.loads(JSON_DATA)

SIC_DATA = []

for row in RAW:
    code = row["code"]
    name = row["description"]
    sic = SicCode(code, name)
    SIC_DATA.append(sic)

class SicRawDataAccess:
    """ Access to raw SIC data """

    def get_sic_data(self):
        """ returns a list of individual SIC codes """
        return SIC_DATA

    def get_sic_ranges(self):
        """ return sic_ranges """
        return SIC_RANGES
