from . import FieldType
from . import FieldValue
from . import FieldTypeRegression
from . import FieldValueRegression

def rec(node, result, randomstate):
    node.randomstate = randomstate
    v = node.pick_value()
    result[node.field_name] = v.get_field_value()

    if v.next_field and len(v.next_field.values) > 0:
        rec(v.next_field, result, randomstate)


def process_type(node, randomstate):

    field = FieldType()
    field.values = []

    for field_key, _ in node.items():

        if field_key not in ('count', 'ratio', 'total'):
            field.field_name = field_key

            for value_key, field_value in node[field_key].items():
                if value_key not in ['total']:
                    field.values.append(process_value(field_value, value_key, randomstate))

    return field

def process_stats(node, randomstate):
    outer_type = None
    current_value = None

    for field_key, _ in node['stats'].items():

        next_type = FieldTypeRegression()
        next_type.field_name = field_key

        value = FieldValueRegression(randomstate)
        value.count = node['stats'][field_key]["count"]
        value.mean = node['stats'][field_key]["mean"]
        value.var = node['stats'][field_key]["var"]
        value.std = node['stats'][field_key]["std"]
        value.min = node['stats'][field_key]["min"]
        value.max = node['stats'][field_key]["max"]
        value.median = node['stats'][field_key]["median"]
        if "best_fit_distribution" in node['stats'][field_key]:
            value.best_fit = node['stats'][field_key]["best_fit_distribution"]
            value.fit_parameter = node['stats'][field_key]["fit_parameter"]
        else:
            value.best_fit = None
            value.fit_parameter = None
        value.next_field = None

        next_type.values = []
        next_type.values.append(value)

        if not outer_type:
            outer_type = next_type

        else:
            current_value.next_field = next_type

        current_value = value

    return outer_type


def process_value(node, value, randomstate):

    field_value = FieldValue()
    field_value.field_value = value
    field_value.ratio = node['ratio']
    field_value.count = node['count']

    if 'stats' in node:
        field_value.next_field = process_stats(node, randomstate)
    else:
        field_value.next_field = process_type(node, randomstate)

    return field_value
