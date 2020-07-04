import numpy as np
import datahub_core.generators as gen

def test_choice():
    df = gen.generate(
        props={
            'region': gen.choice(['NAM', 'EMEA', 'APAC', 'LATAM']),
        },
        count=100,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    found_nam = False
    found_emea = False
    found_apac = False
    found_latam = False


    for row in df['region']:
        if row == 'NAM':
            found_nam = True
        if row == 'EMEA':
            found_emea = True
        if row == 'APAC':
            found_apac = True
        if row == 'LATAM':
            found_latam = True

    assert found_nam
    assert found_emea
    assert found_apac
    assert found_latam


def test_weighting():
    df = gen.generate(
        props={
            'region': gen.choice(
                data=['NAM', 'EMEA', 'APAC', 'LATAM'],
                weights=[0, 0.5, 0.5, 0]),
        },
        count=100,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()


    found_nam = False
    found_emea = False
    found_apac = False
    found_latam = False

    for row in df['region']:
        if row == 'NAM':
            found_nam = True
        if row == 'EMEA':
            found_emea = True
        if row == 'APAC':
            found_apac = True
        if row == 'LATAM':
            found_latam = True

    assert not found_nam
    assert found_emea
    assert found_apac
    assert not found_latam
