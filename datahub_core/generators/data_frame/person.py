import functools
from ..attribute_generators import PersonGenerator

FAKERS = {}

def person(country_field):
    """
    Returns a localised Person

    # Arguments:

    country_field:

        the field name where the framework can find a
        datahub_core.datasets.Country object

    # Returns:

    str:

        The full name of a person

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'region': gen.choice(
                    data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                    weights=[0.1, 0.1, 0.3, 0.5]),
                "country": gen.country_codes(region_field='region'),
                "contact_name": gen.person(country_field='country')
            },
            count=50,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

        print(df)
    """

    return functools.partial(__person, country_field)


def __person(country_field, context=None, df=None, randomstate=None):

    country = df[country_field]
    generator = PersonGenerator(randomstate)
    return generator.make(country)
