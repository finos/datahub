import sys
sys.path.append('../')
sys.path.append('../datahub_core')
sys.path.append('./datahub_core')
sys.path.append('datahub_core')

import numpy as np
import datahub_core.generators as gen

def run(seed=130319810):
    regions = ['NAM', 'EMEA', 'APAC', 'LATAM']
    region_weights = [0.5, 0.3, 0.1, 0.1]

    df = gen.generate(
        props={
            'region': gen.choice(
                data=regions,
                weights=region_weights),
            'country': gen.country_codes(
                region_field='region'),
            'secondary-region': gen.choice(
                data=regions,
                weights=region_weights),                
            'secondary-country': gen.country_codes(
                region_field='secondary-region'),
            'industry': gen.sic_range(),
            'industry_code': gen.sic_industry('industry'),
            'legal-name': gen.company_namer(
                field='industry_code',
                countrycode_field='country'),
            'lei_code': gen.lei_code()
        },
        count=50,
        randomstate=np.random.RandomState(seed)
    ).to_dataframe()

    # Cleanup the country and add the CCY
    df['prefered_ccy'] = df['country'].apply(lambda x: x.currency)
    df['country'] = df['country'].apply(lambda x: x.alpha3_code)

    df['secondary_ccy'] = df['secondary-country'].apply(lambda x: x.currency)
    df['secondary-country'] = df['secondary-country'].apply(lambda x: x.alpha3_code)


    print(df)
    return df

run()
