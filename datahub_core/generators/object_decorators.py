#pylint:disable=unused-argument, line-too-long
import functools
import numpy as np
from datahub_core.data import data_access
from ..libs.data_access import SicRawDataAccess
from .attribute_generators.normal_generator import NormalGenerator
from .attribute_generators.legal_entity_name_generator2 import LegalEntityNameGenerator2
from .attribute_generators.fund_name_generator import FundNameGenerator

def mark_synthetic():
    def decorator(func):
        @functools.wraps(func)
        def decorator_inner(self, *args, **kw):
            return func(self, *args, **kw)
        decorator_inner.synthetic_mark = True
        return decorator_inner
    return decorator

def country_codes():
    return data_access.countries()

def industry_codes():
    return SicRawDataAccess().get_sic_data()

def industry_ranges():
    return SicRawDataAccess().get_sic_ranges()

def company_namer(sic_lamba, _randomsate_lambda=None):
    def decorator(func):
        decorator.make = None
        @functools.wraps(func)
        @mark_synthetic()
        def decorator_inner(self, *args, **kw):
            if decorator.make is None:
                randomstate = __get_random_state(self, _randomsate_lambda)
                gen = LegalEntityNameGenerator2(randomstate).make
                decorator.make = gen

            sic = sic_lamba(self)
            value = decorator.make(sic)
            kw['value'] = value
            return func(self, *args, **kw)
        return decorator_inner
    return decorator

def fund_namer(owner_lamba, _randomsate_lambda=None):
    def decorator(func):
        decorator.make = None
        @functools.wraps(func)
        @mark_synthetic()
        def decorator_inner(self, *args, **kw):
            if decorator.make is None:
                randomstate = __get_random_state(self, _randomsate_lambda)
                gen = FundNameGenerator(randomstate).make
                decorator.make = gen

            owner = owner_lamba(self)
            value = decorator.make(owner)
            kw['value'] = value
            return func(self, *args, **kw)
        return decorator_inner
    return decorator

def normal_sampler(data, _randomstate_lambda=None):
    def decorator(func):
        decorator.gen = None
        @functools.wraps(func)
        @mark_synthetic()
        def decorator_inner(self, *args, **kw):
            if decorator.gen is None:
                randomstate = __get_random_state(self, _randomstate_lambda)
                gen = NormalGenerator(randomstate, data.copy()).make
                decorator.gen = gen
            maker = decorator.gen
            value = maker()
            kw['value'] = value
            return func(self, *args, **kw)
        return decorator_inner
    return decorator

def synthetic_attributes():
    def decorator(original_class):
        original_init = original_class.__init__

        def __init__(self, *args, **kws):
            method_list = [func for func in dir(original_class) if callable(getattr(original_class, func))]
            for method_name in method_list:
                method = getattr(original_class, method_name)
                if hasattr(method, 'synthetic_mark'):
                    method(self)
            original_init(self, *args, **kws)

        original_class.__init__ = __init__
        return original_class
    return decorator

def random_range_int(low, high, _randomstate_lambda=None):
    def decorator(func):
        @functools.wraps(func)
        @mark_synthetic()
        def decorator_inner(self, *args, **kw):
            randomstate = __get_random_state(self, _randomstate_lambda)
            value = randomstate.uniform(low=low, high=high, size=1)[0]
            return func(self, value)
        return decorator_inner
    return decorator

def counter():
    def decorator(func):
        decorator.count = 0
        @functools.wraps(func)
        @mark_synthetic()
        def decorator_inner(self, *args, **kw):
            decorator.count = decorator.count + 1
            value = decorator.count
            #kw['value'] = value
            return func(self, value)
        return decorator_inner
    return decorator

def choice(values, weights=None, _randomstate_lambda=None):
    def decorator(func):
        @functools.wraps(func)
        @mark_synthetic()
        def decorator_inner(self, *args, **kw):
            randomstate = __get_random_state(self, _randomstate_lambda)
            value = randomstate.choice(values, p=weights)
            return func(self, value)
        return decorator_inner
    return decorator

def __get_random_state(self, randomstate_lambda):
    randomstate = np.random
    if callable(randomstate_lambda):
        randomstate = randomstate_lambda(self)
    return randomstate
