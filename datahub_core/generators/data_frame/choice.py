#pylint:disable=unused-argument
import functools
import numpy as np

def choice(data, weights=None):
    """

    Select an element from a list at random with optional weights

    # Arguments:

    data, list:

        A list of objects to choose from, can be of any data type
        weights, list, float: A list of floats, length must be equal
        to the length of the data argument. The sum of weights should = 1

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'region': gen.choice(
                    data=['NAM', 'EMEA', 'APAC', 'LATAM'],
                    weights=[0, 0.5, 0.5, 0]),
            },
            count=100,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

    """
    return functools.partial(
        __choice,
        data=data,
        weights=weights
    )

def __choice(data, weights=None, randomstate=None, df=None):
    if not randomstate:
        randomstate = np.random

    if weights:
        return randomstate.choice(data, p=weights)
    return randomstate.choice(data)


# def weight_normal(data):

# def weight_exponential(data):
