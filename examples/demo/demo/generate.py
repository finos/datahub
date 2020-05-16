import numpy as np
import datahub_core.generators as gen

def run(seed=130319810):

    df = gen.generate(
        props={
            'region': gen.choice(data=['NAM']),
            'country': gen.country_codes(region_field='region'),
            'person_name': gen.person('country'),
            'age': gen.random_range(low=1, high=100, round_dp=0),
        },
        count=50,
        randomstate=np.random.RandomState(seed)
    ).to_dataframe()

    df['ccy'] = df['country'].apply(lambda x: x.currency)
    df['country'] = df['country'].apply(lambda x: x.alpha3_code)

    return df
