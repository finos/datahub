import numpy as np
import datahub_core.analyse as analyse
import datahub_core.models as models
import datahub_core.generators as gen


# def test_generate_model():
#     analyse.run('./tests/train_data.csv', './tests/train_data_output.json',
#                 groups=['b', 'c', 'e', 'f', 'g', 'h', 'i', 'm', 'n'],
#                 cols=['a', 'd', 'j', 'k', 'l'],
#                 fit_distribution=False)

# def test_generate(seed=123456):
#     random = np.random.RandomState(seed)
#     df = gen.generate_from_model(
#         props={},
#         model=models.MarkovModel('./train_data_output.json', random),
#         count=50000
#     ).to_dataframe()

#     df.to_csv('./output2.csv')

#generate_model()
#generate()
