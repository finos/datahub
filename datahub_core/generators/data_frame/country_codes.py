# pylint: disable=unused-argument
import functools
from datahub_core.generators.attribute_generators import CountryCodeGenerator
from datahub_core.generators.data_frame import choice
from ... import metrics as fr_metrics

@fr_metrics.timeit
def country_codes(region_field=None, sampler=choice.bound_choice):
    """
    Generate a country code, yields a country object from datahub_core.datasets.country

    # Arguments:

    region str, optional:

        Region field, must be a string field with a valid region

        ['APAC', 'EMEA', 'NAM', 'LATAM']

     fn_distribution, function, optional:

        defaults to "choice" must be a partial function of the form

        f(data, weights)(df, random_state)

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        result = gen.generate(
            props={
                "region": gen.choice(['NAM']),
                "country": gen.country_codes(region_field="region")
            },
            count=100,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

    """
    return functools.partial(
        __country_codes,
        region_field=region_field,
        sampler=sampler)

@fr_metrics.timeit
def __country_codes(
        region_field=None,
        key=None,
        context=None,
        randomstate=None,
        df=None,
        sampler=None):
    ''' Internal function '''

    region = None

    if region_field and df:
        region = df[region_field]
        key = key + "-" + region

    if not context.has_generator(key):
        generator = CountryCodeGenerator(randomstate, region)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    return generator.make()
