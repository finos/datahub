#pylint:disable=unused-argument

import functools

def counter(counter_state):
    """
    Incremental counter, requires a 'state' object with a function get_one() which returns a number

    # Arguments:

    counter_state, object:
        An object which has a method get_one() which returns an incrementing numeric value

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        counter_state = gen.CounterState()

        df = gen.generate(
            props={
                'id': gen.counter(counter_state)
            },
            count=100,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

    """

    return functools.partial(__counter, counter_state)

def __counter(counter_state, df=None, randomstate=None):
    return counter_state.get_one()
