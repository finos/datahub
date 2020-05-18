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

    # uncomment to plot!
    # import matplotlib.pyplot as plt
    # plt.show()
