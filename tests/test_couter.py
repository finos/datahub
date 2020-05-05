import numpy as np
import datahub_core.generators as gen

def test_address_generation():

    counter_state = gen.CounterState()

    df = gen.generate(
        props={
            'data': gen.counter(counter_state)
        },
        count=100,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    count = 1
    for row in df['data']:
        assert row == count
        count = count + 1
