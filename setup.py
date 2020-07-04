import os
from setuptools import setup, find_packages

def __path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

VERSION = '0.9.10'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(    
    name='datahub_core-grovesy',
    version=VERSION,
    url='https://github.com/finos/datahub',        
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'datahub_core': [
        './data/codes.txt',
        './data/company_names.txt',
        './data/country-codes.txt',
        './data/sic-codes.txt',
        './data/sic-conventions.json',
        './data/sic-ranges.txt',
        './data/addresses/US.json',
        './data/funds/asset_class.csv',
        './data/funds/classes.csv',
        './data/funds/asset_class.csv',
        './data/funds/dividend_treatment.csv',
        './data/funds/regions.csv',
        './data/**'
    ]},
    author='grovesy',
    author_email="paul.groves@citi.com",
    description='Synthetic data generation tools for financial markets',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=True,
    
)
