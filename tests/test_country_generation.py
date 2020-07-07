import numpy as np
import datahub_core.generators as gen
import datahub_core.data as data

def test_generated_regions_are_correct():
    result = gen.generate(
        props={"region": gen.choice(data.regions())},
        count=100,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    assert len(result) == 100
    region_list = data.regions()

    for row in result['region']:
        assert row in region_list


def test_countries_are_in_nam_target_region():
    result = gen.generate(
        props={
            "region": gen.choice(['NAM']),
            "country": gen.country_codes(region_field="region")
        },
        count=100,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    country_list = data.countries(region="NAM")

    for row in result['country']:
        assert row in country_list


def test_countries_are_in_not_in_nam_target_region():
    result = gen.generate(
        props={
            "region": gen.choice(['NAM']),
            "country": gen.country_codes(region_field="region", sampler=gen.bound_choice)
        },
        count=100,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    country_list = data.countries(region="EMEA")

    for row in result['country']:
        assert row not in country_list
