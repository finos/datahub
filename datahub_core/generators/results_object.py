import pandas as pd

class ResultObject:

    results = []

    def __init__(self, results):
        self.results = results

    def items(self):
        return self.results

    def count(self):
        return len(self.results)

    def to_dataframe(self):
        return pd.DataFrame(self.results)
