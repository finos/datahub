import numpy as np
import datahub_core.generators as gen

def test_correct_number_of_rows_are_generated():

    df = gen.generate_from_model(
        props={
            'region' : gen.normal_sampler(
                data=['EMEA', 'NAM', 'APAC', 'LATAM'])
        },
        count=1000,
        randomstate=np.random.RandomState()
    ).to_dataframe()

    print(df)
