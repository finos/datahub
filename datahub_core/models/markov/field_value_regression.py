#pylint:disable=line-too-long
import scipy.stats as st
from ... import Printable

class FieldValueRegression(Printable):
    field_value = 0
    count: None
    mean: None
    var: None
    std: None
    min: None
    max: None
    median: None
    next_field: None
    best_fit: None
    fit_parameter: ''

    def __init__(self, randomstate):
        self.randomstate = randomstate

    def get_field_value(self):

        if self.count > 1:
            if self.best_fit is not None:
                best_dist = getattr(st, self.best_fit)
                params = list(map(float, self.fit_parameter.split(',')))
                arg = params[:-2]
                loc = params[-2]
                scale = params[-1]
                s = best_dist.rvs(*arg, loc=loc, scale=scale) if arg else best_dist.rvs(loc=loc, scale=scale)
                while s < self.min or s > self.max:
                    s = best_dist.rvs(*arg, loc=loc, scale=scale) if arg else best_dist.rvs(loc=loc, scale=scale)
                return round(s, 2)

        mean, std = self.mean, self.std
        s = self.randomstate.normal(mean, std, 1)
        while s[0] < self.min or s[0] > self.max:
            s = self.randomstate.normal(mean, std, 1)
        return round(s[0], 2)
