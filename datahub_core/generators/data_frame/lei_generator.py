#pylint:disable=unused-argument
import functools
import numpy as np
from ... import metrics as fr_metrics
from ..attribute_generators import LeiGenerator

@fr_metrics.timeit
def lei_code():
    """
    Generates an LEI code

    # Returns:

        string, and LEI code

    # Example:

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'lei': gen.lei_code()
            },
            count=50,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

    """
    return functools.partial(__lei_code)

@fr_metrics.timeit
def __lei_code(key=None, context=None, randomstate=None, df=None):
    """ Internal function, do not use """
    if randomstate is None:
        randomstate = np.random

    if not context.has_generator(key):
        generator = LeiGenerator(randomstate)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    return generator.make()
