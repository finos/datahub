""" Normal sampler """
import scipy
from ... import metrics as fr_metrics

class NormalGenerator:
    """ Normal sampler, uses a list of items and draws a
    sample from it based on a normal distribution """


    @fr_metrics.timeit
    def __init__(self, random_state, items=None, size=1000, mu=0, sigma=None):        
        self.random_state = random_state
        self.items = items
        self.data = []
        self.current = 0

        # setup a normal distribution function to create samples
        lower, upper = 0, len(self.items)

        if not sigma:
            sigma = upper / 4

        normal_gen = scipy.stats.truncnorm(
            (lower - mu) / sigma, (upper - mu) / sigma,
            loc=mu,
            scale=sigma)

        normal_gen.random_state = self.random_state
        indices = normal_gen.rvs(size, random_state=self.random_state)

        for index in indices:
            item = self.items[int(index)]
            self.data.append(item)



    @fr_metrics.timeit
    def make(self):
        """ Sample an item """

        if self.current >= len(self.data):
            self.current = 0

        item = self.data[self.current]

        self.current += 1
        return item
