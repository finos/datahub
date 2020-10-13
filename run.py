import numpy as np
import datahub_core.analyse as analyse
import datahub_core.models as models
import datahub_core.generators as gen


def test_generate_model():
    analyse.run('./train_data.csv', './train_data_output3.json',
                groups=['b', 'c', 'e', 'f', 'g', 'h', 'i', 'm', 'n'],
                cols=['a', 'd', 'j', 'k', 'l'],
                fit_distribution=False)

def test_generate_data(seed=123456):
    random = np.random.RandomState(seed)
    df = gen.generate_from_model(
        props={},
        model=models.MarkovModel('./train_data_output3.json', random),
        count=100000
    ).to_dataframe()


    df['a'] = df['a'].map(lambda x: int(x))
    df['d'] = df['d'].map(lambda x: int(x))
    df['j'] = df['j'].map(lambda x: int(x))
    df['k'] = df['k'].map(lambda x: int(x))
    df['l'] = df['l'].map(lambda x: int(x))

    df.to_csv('./train_data_output3.csv')

test_generate_model()
test_generate_data()
