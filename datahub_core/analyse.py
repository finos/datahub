#pylint:disable=broad-except, line-too-long, unused-argument, unnecessary-lambda, too-many-locals
import io
import pprint
import json
import warnings
import multiprocessing
import numpy as np
import pandas as pd
import scipy.stats as st
from joblib import Parallel, delayed


pp = pprint.PrettyPrinter(indent=2)

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 20000)

def fit_single_distribution(distribution, data, x, y):
    sse = np.inf
    params = []
    try:
        # Ignore warnings from data that can't be fit
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore')

            # fit dist to data
            params = distribution.fit(data)

            # Separate parts of parameters
            arg = params[:-2]
            loc = params[-2]
            scale = params[-1]

            # Calculate fitted PDF and error with fit in distribution
            pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
            sse = np.sum(np.power(y - pdf, 2.0))
    except Exception:
        pass
    return (distribution, sse, params)

def best_fit_distribution(data, bins='auto', ax=None):
    """Model data by finding best fit distribution to data"""
    # Get histogram of original data
    y, x = np.histogram(data, bins=bins, density=True)
    x = (x + np.roll(x, -1))[:-1] / 2.0

    # Distributions to check
    distributions = [
        st.alpha, st.anglit, st.arcsine, st.beta, st.betaprime,
        st.bradford, st.burr, st.cauchy, st.chi, st.chi2,
        st.cosine, st.dgamma, st.dweibull, st.erlang, st.expon,
        st.exponnorm, st.exponweib, st.exponpow, st.f, st.fatiguelife,
        st.fisk, st.foldcauchy, st.foldnorm, st.frechet_r, st.frechet_l,
        st.genlogistic, st.genpareto, st.gennorm, st.genexpon, st.genextreme,
        st.gausshyper, st.gamma, st.gengamma, st.genhalflogistic,
        st.gilbrat, st.gompertz, st.gumbel_r, st.gumbel_l, st.halfcauchy,
        st.halflogistic, st.halfnorm, st.halfgennorm, st.hypsecant, st.invgamma,
        st.invgauss, st.invweibull, st.johnsonsb, st.johnsonsu, st.ksone,
        st.kstwobign, st.laplace, st.levy, st.levy_l, st.levy_stable,
        st.logistic, st.loggamma, st.loglaplace, st.lognorm, st.lomax,
        st.maxwell, st.mielke, st.nakagami, st.ncx2, st.ncf,
        st.nct, st.norm, st.pareto, st.pearson3, st.powerlaw,
        st.powerlognorm, st.powernorm, st.rdist, st.reciprocal, st.rayleigh,
        st.rice, st.recipinvgauss, st.semicircular, st.t, st.triang, st.truncexpon,
        st.truncnorm, st.tukeylambda, st.uniform, st.vonmises, st.vonmises_line,
        st.wald, st.weibull_min, st.weibull_max, st.wrapcauchy
    ]

    # Best holders
    best_distribution = st.norm
    best_params = (0.0, 1.0)
    best_sse = np.inf

    # Estimate distribution parameters from data
    num_cores = multiprocessing.cpu_count()
    results = Parallel(n_jobs=num_cores)(delayed(fit_single_distribution)(distribution, data, x, y) for distribution in distributions)

    for item in results:
        if best_sse > item[1] > 0:
            best_distribution = item[0]
            best_params = item[2]
            best_sse = item[1]

    return (best_distribution.name, best_params)

def create_initial_df(input_filename, groups, cols, aggregations, fit_distribution=False):
    """ create dataframe from input csv file """
    df_raw = pd.read_csv(input_filename)

    all_cols = groups.copy() + cols

    csv_headers = []

    for c in cols:
        for a in aggregations:
            csv_headers.append(f'{c}_{a}')

    dis_df = df_raw[all_cols].copy()
    df = df_raw[all_cols].groupby(groups).agg(aggregations)
    s_buf = io.StringIO()
    df.to_csv(s_buf, header=csv_headers)
    s_buf.seek(0)
    df = pd.read_csv(s_buf)
    df = df.replace({pd.np.nan: None})

    if fit_distribution is True:
        ## Calculate the best fit distribution name and parameters
        dis_df = dis_df.groupby(groups)
        for key in dis_df.groups.keys():
            for c in cols:
                data = dis_df.get_group(key)[c]
                best_fit_name, best_fit_params = best_fit_distribution(data)
                index = (df[groups] == pd.DataFrame([key], columns=groups).loc[0]).apply(lambda x: np.all(x), axis=1)

                print("Column: " + c + ' is best fit for ' + best_fit_name)
                df.loc[index, c + '_best_fit_distribution'] = best_fit_name
                df.loc[index, c + '_fit_parameter'] = ','.join(map(str, best_fit_params))
    return df

def create_tree_structure(df, groups, cols, aggregations, fit_distribution=False):
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
                    if fit_distribution:
                        result['stats'][c]['best_fit_distribution'] = row[f'{c}_best_fit_distribution']
                        result['stats'][c]['fit_parameter'] = row[f'{c}_fit_parameter']

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

def run(input_filename, output_filename, groups, cols, fit_distribution=False):
    """ run!"""

    aggregations = ['count', 'mean', 'var', 'std', 'min', 'max', 'median']
    df = create_initial_df(input_filename, groups, cols, aggregations, fit_distribution)
    results = create_tree_structure(df, groups, cols, aggregations, fit_distribution)
    crawl_tree_and_set_ratios(results)

    with open(output_filename, 'w') as outfile:
        json.dump(results, outfile, default=default, indent=2)

def default(o):
    """ handles converting np ints to python ints for json dumping """
    if isinstance(o, np.int64):
        return int(o)
    raise TypeError
