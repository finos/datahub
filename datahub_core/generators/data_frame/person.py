import functools
from ... import metrics as fr_metrics
from ..attribute_generators import PersonGenerator

FAKERS = {}

@fr_metrics.timeit
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
    """

    return functools.partial(__person, country_field)

@fr_metrics.timeit
def __person(country_field, key=None, context=None, df=None, randomstate=None):

    country = df[country_field]

    if not context.has_generator(key):
        generator = PersonGenerator(randomstate)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    return generator.make(country)
