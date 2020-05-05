from ... import Printable

class FieldType(Printable):
    field_name: str
    values: []
    randomstate: None

    def pick_value(self):
        weights = []
        values = []
        index = 0
        for x in self.values:
            values.append(index)
            weights.append(x.ratio)
            index += 1

        return self.randomstate.choice(self.values, p=weights)
