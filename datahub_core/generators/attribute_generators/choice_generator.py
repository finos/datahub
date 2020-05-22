from ... import metrics as fr_metrics
class ChoiceGenerator():

    @fr_metrics.timeit
    def __init__(self, random_state, data, weights=None):
        print("--- NEW CHOiCE --- ")
        self.random_state = random_state
        self.data = data
        self.weights = weights

    @fr_metrics.timeit
    def make(self):
        if self.weights:
            return self.random_state.choice(self.data, p=self.weights)

        return self.random_state.choice(self.data)
