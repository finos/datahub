import numpy as np
import datahub_core.generators as gen
import datahub_core.data as data

def test_correct_number_of_rows_are_generated():
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
