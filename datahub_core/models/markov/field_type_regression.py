from ... import Printable

class FieldTypeRegression(Printable):
    field_name: str
    values: None
    randomstate: None

    def pick_value(self):
        return self.values[0]
