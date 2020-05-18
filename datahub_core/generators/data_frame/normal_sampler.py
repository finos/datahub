#pylint:disable=unused-argument
import functools
from ... import metrics as fr_metrics
from ..attribute_generators import NormalGenerator

@fr_metrics.timeit
def normal_sampler(data, mu=0, sigma=None):
    return functools.partial(__normal_sampler, data=data, mu=mu, sigma=sigma)

@fr_metrics.timeit
def __normal_sampler(data, mu=0, sigma=None, key=None, context=None, randomstate=None, df=None):

    if not context.has_generator(key):
        generator = NormalGenerator(randomstate, data.copy(), context.record_count, mu, sigma)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    value = generator.make()
    return value
