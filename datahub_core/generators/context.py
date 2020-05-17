
class Context:
    
    recordCount = 0
    generators = {}

    def __init__(self, record_count):
        self.record_count = record_count
    
    def addGenerator(self, key, generator):
        self.generators[key] = generator
    
    def hasGenerator(self, key):
        return key in self.generators

    def getGenerator(self, key):
        return self.generators[key]
