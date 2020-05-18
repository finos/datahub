""" legal_entity_name_generator """
import numpy
from ... import resource
from ... import metrics as fr_metrics
from ...libs.markov_chains import MName

@fr_metrics.timeit
def prep_file(file_name):
    items = []

    with open(file_name) as files:
        for newline in files:
            items.append(newline)
    return items

NAMES = prep_file(resource('company_names.txt'))


class CompanyNameMarkov:
    """ Generates legal entity names using Markov-Chains """

    random_state: numpy.random.RandomState
    sic = {}

    @fr_metrics.timeit
    def __init__(self, seed):
        self.random_state = seed
        self.namer = MName(NAMES, self.random_state, 3)


    @fr_metrics.timeit
    def make(self, model):
        """ Generate a name using markov chains """
        masks = model['masks']
        full_name = self.random_state.choice(masks)

        for _ in range(full_name.count('{x}')):
            while True:
                name = self.namer.make()

                if len(name) < 3:
                    continue

                if len(name) > 12:
                    continue

                break

            full_name = full_name.replace('{x}', name, 1)

        return full_name
