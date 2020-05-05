""" Normal sampler """
import scipy
from ... import metrics as fr_metrics

class NormalGenerator:
    """ Normal sampler, uses a list of items and draws a
    sample from it based on a normal distribution """
    items = []
    data = []
    current = 0

    def __init__(self, random_state, items):
        self.random_state = random_state
        self.items = items

        # setup a normal distribution function to create samples
        lower, upper = 0, len(self.items)
        m_u, sigma = 0, upper / 4

        normal_gen = scipy.stats.truncnorm(
            (lower - m_u) / sigma, (upper - m_u) / sigma,
            loc=m_u,
            scale=sigma)

        normal_gen.random_state = self.random_state
        indices = normal_gen.rvs(1000, random_state=self.random_state)

        data = []
        for index in indices:
            item = self.items[int(index)]
            data.append(item)
        self.data = data

    @fr_metrics.timeit
    def make(self):
        """ Sample an item """

        if self.current >= len(self.data):
            self.current = 0

        item = self.data[self.current]

        self.current += 1
        return item
