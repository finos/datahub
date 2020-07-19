import numpy as np
import datahub_core.analyse as analyse
import datahub_core.models as models
import datahub_core.generators as gen

def test_generation_of_data():
    analyse.run(
        './tests/output.csv', './tests/model.json',
        groups=['region', 'country', 'sic_code', 'industry', 'sic_name'],
        cols=['aum'],
        fit_distribution=False)

def test_generation(seed=123456):
    random = np.random.RandomState(seed)
    df = gen.generate_from_model(
        model=models.MarkovModel('./tests/model.json', random),
        props={},
        count=50, randomstate=random
    ).to_dataframe()

    print(df)
