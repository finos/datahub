
class Context:

    record_count = 0
    generators = None

    def __init__(self, record_count):        
        self.record_count = record_count
        self.generators = {}
        self.record_count = record_count

    def add_generator(self, key, generator):
        self.generators[key] = generator

    def has_generator(self, key):
        return key in self.generators

    def get_generator(self, key):
        return self.generators[key]
