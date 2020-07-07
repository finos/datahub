import json
from .generator import rec
from .generator import process_type

class MarkovModel:

    def __init__(self, filename, randomstate):        
        self.randomstate = randomstate

        with open(filename, 'r') as f:
            data = json.load(f)

        self.type_node = process_type(data, randomstate)

    def make_one(self):
        result = {}
        rec(self.type_node, result, self.randomstate)
        return result
