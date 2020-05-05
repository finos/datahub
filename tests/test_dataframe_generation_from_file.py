import numpy as np
import datahub_core.generators as gen
from datahub_core.models import MarkovModel
RS = np.random.RandomState(13031981)

MODEL = MarkovModel(filename='./tests/client_data.json', randomstate=RS)

RESULT = gen.generate_from_model(
    props={
        "country": gen.country_codes(region_field='region'),
        "ev": gen.random_range(high=100000, low=10000000),
        "address": gen.address(country_field='country'),
        "contact_name": gen.person(country_field='country'),
        "client_name": gen.company_namer(
            field='client_type',
            field_type='client_type',
            countrycode_field='country'
        )},
    count=50, model=MODEL)

def test_correct_number_of_rows_are_generated():
    df = RESULT.to_dataframe()

    # remap obects into flat table
    df['country'] = df['country'].map(lambda x: x.alpha3_code)
    df['city'] = df['address'].map(lambda x: x.city)
    df['state'] = df['address'].map(lambda x: x.state)
    del df['address']

    print(df)
