#pylint:disable=unused-argument
import functools
import scipy
import numpy as np
from ..attribute_generators import NormalGenerator

def normal_sampler(data):
    return functools.partial(__normal_sampler, data=data)


def __normal_sampler(data, context=None, randomstate=None, df=None):
    gen = NormalGenerator(randomstate, data.copy())
    value = gen.make()
    return value


def normal(lower=0, upper=1.0, mu=0, sigma=None, randomstate=None, df=None):
    return functools.partial(__normal, lower, upper, mu, sigma)


def __normal(lower=0, upper=1.0, mu=0, sigma=None, context=None, randomstate=None, df=None):

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
