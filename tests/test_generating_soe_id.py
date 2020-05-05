import numpy as np
import datahub_core.generators as gen

def test_correct_number_of_rows_are_generated():
    df = gen.generate(
        props={
            'region': gen.choice(
                data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                weights=[0.1, 0.1, 0.3, 0.5]),
            "country": gen.country_codes(region_field='region'),
            "contact_name": gen.person(country_field='country'),
            "soe_id": gen.soe_id(name_field="contact_name")
        },
        count=50,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    print(df)
