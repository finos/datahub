#pylint:disable=unused-argument,line-too-long
import functools
from ... import metrics as fr_metrics
from ..attribute_generators import NormalGenerator

@fr_metrics.timeit
def normal_sampler(data, mu=0, sigma=None):
    """
    Picks elements from an array to a Normal distribution. Probability of selection
    is in the order of the data array, e.g. data[0] has a higher probability than
    data[1], data[2], data[3] and so on.

    ## Arguments:
    data, array

    Array of elements to select from. Items at the start of the array have a higher
    probability than items at the back of the array

    mu, float:
    The mean https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html

    sigma, float:
    The standard deviation https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html

    ## Returns:

    ## Example:
    import numpy as np
    import datahub_core.generators as gen
    import datahub_core.data as data

    def test_correct_number_of_rows_are_generated():

        df = gen.generate_from_model(
            props={
                'country': gen.normal_sampler(
                    mu=1,
                    data=data.countries())
            },
            count=100000,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

        df['country'] = df['country'].map(lambda x: x.alpha2_code)


        ax = df['country'].value_counts().plot(kind='bar')
        ax = df['country'].value_counts().plot(x='month', linestyle='-', marker='o', ax=ax)
        ax.set_xlabel("Country")
        ax.set_ylabel("Count")
        plt.show()

    """

    return functools.partial(__normal_sampler, data=data, mu=mu, sigma=sigma)

def bound_normal(mu, sigma=None):
    return functools.partial(NormalGenerator, mu=mu, sigma=None)

@fr_metrics.timeit
def __normal_sampler(data, mu=0, sigma=None, key=None, context=None, randomstate=None, df=None):

    if not context.has_generator(key):
        generator = NormalGenerator(random_state=randomstate, items=data, size=context.record_count, mu=mu, sigma=sigma)
        context.add_generator(key, generator)

    generator = context.get_generator(key)

    value = generator.make()
    return value
