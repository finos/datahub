""" top line doc """
import functools
import numpy as np
from ..attribute_generators import LegalEntityNameGenerator2


def company_namer(field, field_type='sic', countrycode_field=None,):
    """

    Generates a company name based with localisation parameters
    for the country and industry code.

    # Arguments:

    field, str:

        The field from the dataframe which contains the industry_code.

    field_type, str, optional:

        The industry_code convention, either SIC or client_type

    countrycode_field, str, optional:

        Optional field for the country, if not specified selects countries at random

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'region': gen.choice(
                    data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                    weights=[0.1, 0.1, 0.3, 0.5]),
                "country": gen.country_codes(region_field='region'),
                "client_type": gen.choice(data=data.client_types()),
                "client_name": gen.company_namer(
                    field='client_type',
                    field_type='client_type',
                    countrycode_field='country'
                )},
            count=50,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

        print(df)

    """
    return functools.partial(
        __company_namer,
        field=field,
        field_type=field_type,
        countrycode_field=countrycode_field)


def __company_namer(field, field_type='sic', countrycode_field=None, context=None, randomstate=None, df=None):
    
    if randomstate is None:
        randomstate = np.random

    if 'LegalEntityNameGenerator2' not in context:
        context['LegalEntityNameGenerator2'] = LegalEntityNameGenerator2(randomstate)

    
    gen = context['LegalEntityNameGenerator2']

    field_value = df[field]

    if countrycode_field:
        countrycode_field = df[countrycode_field]

    if field_type == 'sic':
        value = gen.make(field_value, countrycode_field)

    elif field_type == 'client_type':
        value = gen.make_clienttype(field_value, countrycode_field)

    else:
        return None

    return value
