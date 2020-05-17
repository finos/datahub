#pylint:disable=unused-argument
import functools
import scipy
import numpy as np
from ... import metrics as fr_metrics
from ..attribute_generators import NormalGenerator

@fr_metrics.timeit
def normal_sampler(data):
    return functools.partial(__normal_sampler, data=data)

@fr_metrics.timeit
def __normal_sampler(data, key=None, ontext=None, randomstate=None, df=None):

    if not context.hasGenerator(key):
        generator = NormalGenerator(randomstate, data.copy())
        context.addGenerator(key, gen)
    
    generator = context.getGenerator(key)
    
    value = generator.make()
    return value

@fr_metrics.timeit
def normal(lower=0, upper=1.0, mu=0, sigma=None, randomstate=None, df=None):
    return functools.partial(__normal, lower, upper, mu, sigma)

@fr_metrics.timeit
def __normal(lower=0, upper=1.0, mu=0, sigma=None, key=None, context=None, randomstate=None, df=None):

    if not randomstate:
        randomstate = np.random

    if not sigma:
        sigma = upper / 4



    normal_gen = scipy.stats.truncnorm(
        (lower - mu) / sigma, (upper - mu) / sigma,
        loc=mu,
        scale=sigma)

    normal_gen.random_state = randomstate

    normal_gen.rvs(1000, random_state=randomstate)
