from ... import Printable
from . import FieldType

class FieldValue(Printable):

    field_value: None
    ratio: 0
    count: 0
    next_field: FieldType

    def get_field_value(self):
        return self.field_value
