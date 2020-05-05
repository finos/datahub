import numpy as np
import datahub_core.generators as gen

def test_correct_number_of_rows_are_generated():

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

    print(df)
