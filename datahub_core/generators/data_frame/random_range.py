#pylint:disable=unused-argument

import functools
import numpy as np
from ... import metrics as fr_metrics

@fr_metrics.timeit
def random_range(low=0, high=1000000, round_dp=2):
    """
        Generates a random number within a range rounded to the desired decimal points

        # Arguments:

        low, numeric, optional:

            The lowerbound number defaults to 0

        high, numeric, optional

            The upper bound number, defaults to 1000000

        dp, int, optional

            The number of decimal points the generated number is rounded to.
            defaults to 2

        # Example:

            import numpy as np
            import datahub_core.generators as ge

            df = gen.generate(
                props={
                    "ev": gen.random_range(
                        high=100000,
                        low=10000000,
                        dp=2)
                },
                count=50,
                randomstate=np.random.RandomState(13031981)
            ).to_dataframe()
    """
    return functools.partial(
        __random_range,
        low=low,
        high=high,
        round_dp=round_dp)

@fr_metrics.timeit
def __random_range(
        low=0,
        high=1000000,
        round_dp=2,
        key=None,
        context=None,
        randomstate=None,
        df=None):

    state = np.random
    if randomstate:
        state = randomstate
    value = state.uniform(low=low, high=high, size=1)[0]
    return round(value, round_dp)
