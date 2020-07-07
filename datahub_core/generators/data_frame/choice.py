#pylint:disable=unused-argument
import functools
import numpy as np
from ..attribute_generators import ChoiceGenerator
from ... import metrics as fr_metrics


@fr_metrics.timeit
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


def bound_choice():
    return functools.partial(ChoiceGenerator, weights=None)


@fr_metrics.timeit
def __choice(data, weights=None, key=None, context=None, randomstate=None, df=None):
    if not randomstate:
        randomstate = np.random

    if not context.has_generator(key):
        generator = ChoiceGenerator(randomstate, data=data, weights=weights)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    return generator.make()
