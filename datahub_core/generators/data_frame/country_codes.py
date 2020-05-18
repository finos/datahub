# pylint: disable=unused-argument
import functools
from .. import choice
from ... import metrics as fr_metrics
from ...libs.data_access import CountryDataAccess

@fr_metrics.timeit
def country_codes(region_field=None, fn_distribution=choice):
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
        fn_distribution=fn_distribution)

@fr_metrics.timeit
def __country_codes(
        region_field=None,
        fn_distribution=choice,
        key=None,
        context=None,
        randomstate=None,
        df=None):
    ''' Internal function '''
    countries = []

    if region_field and df:
        region = df[region_field]
        countries = CountryDataAccess().get(region)
    else:
        countries = CountryDataAccess().get()

    value = fn_distribution(data=countries, weights=None)(df=df, randomstate=randomstate)

    return value
