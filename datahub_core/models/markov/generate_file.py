#pylint:disable=too-many-locals
import io
import json
import pandas as pd
import numpy as np

def create_initial_df(input_filename, groups, cols, aggregations):
    """ create dataframe from input csv file """
    df_raw = pd.read_csv(input_filename)

    all_cols = groups.copy() + cols

    csv_headers = []

    for c in cols:
        for a in aggregations:
            csv_headers.append(f'{c}_{a}')
    
    df = df_raw[all_cols].groupby(groups).agg(aggregations)
    s_buf = io.StringIO()
    df.to_csv(s_buf, header=csv_headers)
    s_buf.seek(0)
    df = pd.read_csv(s_buf)
    df = df.replace({pd.np.nan: None})
    
    return df

def create_tree_structure(df, groups, cols, aggregations):
    """ Takes the aggregated row data in the dataframe, produce a tree
        The tree counts all the child elements as it builds
    """

    results = {}

    ## build up the initial structure
    for _, row in df.iterrows():
        stack = []
        result = results

        for field in groups:
            value = row[field]
            stack.append((field, value))
            if field not in result:
                result[field] = {
                    'total': 0
                }

            result = result[field]

            if value not in result:
                result[value] = {
                    'count': 0,
                    'ratio': 0
                }

            result = result[value]

            if field == groups[-1]:
                result['stats'] = {}

                for c in cols:
                    result['stats'][c] = {}
                    for a in aggregations:
                        result['stats'][c][a] = row[f'{c}_{a}']

                stack_r = results
                for s in stack:
                    (field, value) = s
                    count = result['stats'][cols[0]]['count']
                    total = stack_r[field]['total']
                    stack_r[field]['total'] = total + count
                    stack_r[field][value]['count'] = stack_r[field][value]['count'] + count
                    stack_r = stack_r[field][value]
            
        stack = []
    return results

def crawl_tree_and_set_ratios(result):
    """ crawl the tree, and sumarise the ratio's """
    for field in result:

        # Ignore these keys
        if field in ['ratio', 'count', 'stats']:
            continue

        # Get the total key
        total = result[field]['total']

        for value in result[field]:
            if value == 'total':
                continue

            # Set the ratio field
            result[field][value]['ratio'] = result[field][value]['count'] / total

            # Recurse
            crawl_tree_and_set_ratios(result[field][value])

def run(input_filename, output_filename, groups, cols):
    """ run!"""

    aggregations = ['count', 'mean', 'var', 'std', 'min', 'max', 'median']
    df = create_initial_df(input_filename, groups, cols, aggregations)
    results = create_tree_structure(df, groups, cols, aggregations)
    crawl_tree_and_set_ratios(results)

    with open(output_filename, 'w') as outfile:
        json.dump(results, outfile, default=default, indent=2)

def default(o):
    """ handles converting np ints to python ints for json dumping """
    if isinstance(o, np.int64):
        return int(o)
    raise TypeError
