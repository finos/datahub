import functools
from ... import metrics as fr_metrics
from ..attribute_generators import AddressGenerator

@fr_metrics.timeit
def address(country_field):
    """

    Generates a localised address

    # Arguments:

    country_field, str:

        The field in the generated dataset which holds the country object.
        It must be a country object from datahub_core.datasaets.country

    # Example:


        import numpy as np
        import datahub_core.generators as gen

        def test_address_generation():
            df = gen.generate(
                props={
                    'region': gen.choice(['NAM', 'EMEA', 'APAC', 'LATAM']),
                    'country': gen.country_codes(region_field='region'),
                    'address': gen.address('country')
                },
                count=100,
                randomstate=np.random.RandomState(13031981)
            ).to_dataframe()


        ## post process, adress is an object
        df['country'] = df['country'].apply(lambda x: x.alpha2_code)
        df['address_1'] = df['address'].apply(lambda x: x.address_1)
        df['address_2'] = df['address'].apply(lambda x: x.address_2)
        df['city'] = df['address'].apply(lambda x: x.city)
        df['state'] = df['address'].apply(lambda x: x.state)
        df['postal)code'] = df['address'].apply(lambda x: x.postal_code)

        del df['address']

    """
    return functools.partial(
        __address,
        country_field=country_field)

@fr_metrics.timeit
def __address(country_field, key=None, context=None, randomstate=None, df=None):
    country_code = df[country_field]

    if not context.has_generator(key):
        generator = AddressGenerator(randomstate)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    return generator.make(country_code)
