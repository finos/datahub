import matplotlib.pyplot as plt
import numpy as np
import datahub_core.generators as gen
import datahub_core.data as data


def test_normal_sampler_outside():

    df = gen.generate_from_model(
        props={
            'country': gen.normal_sampler(
                data=data.countries(),
                mu=1)
        },
        count=100000,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    df['country'] = df['country'].map(lambda x: x.alpha2_code)


    ax = df['country'].value_counts().plot(kind='bar')
    ax = df['country'].value_counts().plot(x='month', linestyle='-', marker='o', ax=ax)
    ax.set_xlabel("Country")
    ax.set_ylabel("Count")

    #uncomment to plot!

    plt.show()


def test_normal_sampler_bound():

    df = gen.generate_from_model(
        props={
            'country': gen.country_codes(sampler=gen.bound_normal)
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
