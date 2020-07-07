#pylint:disable=unused-argument
import functools
import numpy as np
from ... import metrics as fr_metrics
from ..attribute_generators import SicCodeGenerator
from ..attribute_generators import SicRangeGenerator

@fr_metrics.timeit
def sic_industry(sic_range_field):
    """
    Generates an Industry SIC dode based on a selected industry sector (SicRange)

    # Arguments:
    sic_range_filed: str,

        Must be a datahub_core.datasets.SicRange object with the attributes:

        {
            start int,
            end int,
            name str
        }

    # Returns:

        object, datahub_core.datasets.SicCode

        {
            start int,
            end int,
            name str
        }

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'region': gen.choice(
                    data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                    weights=[0.1, 0.1, 0.3, 0.5]),
                'sic_range' : gen.sic_range(),
                'sic': gen.sic_industry(sic_range_field='sic_range'),
                'country': gen.country_codes(region_field='region'),
                'client_name': gen.company_namer(
                    field='sic',
                    field_type='sic',
                    countrycode_field='country'
                )},
            count=50,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

        df['sic_range'] = df['sic_range'].apply(lambda x: x.name)
        df['sic'] = df['sic'].apply(lambda x: x.name)
        df['country'] = df['country'].apply(lambda x: x.alpha3_code)

    """
    return functools.partial(__sic_industry, sic_range_field)

@fr_metrics.timeit
def __sic_industry(sic_field, key=None, context=None, randomstate=None, df=None):
    """ Internal function, do not use """
    if randomstate is None:
        randomstate = np.random

    if not context.has_generator(key):
        generator = SicCodeGenerator(randomstate)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    sic = df[sic_field]
    return generator.make(sic.start, sic.end)

@fr_metrics.timeit
def sic_range():
    """
    Generates an Industry SIC Sector

    # Arguments:

        None

    # Returns:

        object, datahub_core.datasets.SicRange

        {
            start, int
            end int
            name str
        }

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'region': gen.choice(
                    data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                    weights=[0.1, 0.1, 0.3, 0.5]),
                'sic_range' : gen.sic_range(),
                'sic': gen.sic_industry(sic_range_field='sic_range'),
                'country': gen.country_codes(region_field='region'),
                'client_name': gen.company_namer(
                    field='sic',
                    field_type='sic',
                    countrycode_field='country'
                )},
            count=50,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

        df['sic_range'] = df['sic_range'].apply(lambda x: x.name)
        df['sic'] = df['sic'].apply(lambda x: x.name)
        df['country'] = df['country'].apply(lambda x: x.alpha3_code)

    """

    return functools.partial(__sic_range)

@fr_metrics.timeit
def __sic_range(key=None, context=None, randomstate=None, df=None):
    if randomstate is None:
        randomstate = np.random

    if not context.has_generator(key):
        generator = SicRangeGenerator(randomstate)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    return generator.make()
