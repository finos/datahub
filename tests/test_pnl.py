import numpy as np
import datahub_core.generators as gen

def test_correct_number_of_rows_are_generated():

    df = gen.generate(
        props={
            'firm_account': gen.choice(data=['A', 'B', 'C']),
            'region': gen.choice(data=['NAM', 'EMEA', 'LATAM', 'APAC']),
            'country': gen.country_codes(region_field="region"),
            'intraday_pnl': gen.random_range(low=-1000, high=1000, round_dp=2),
            'trade_year': gen.choice(
                data=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
        },
        count=50,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    df['ccy'] = df['country'].apply(lambda x: x.currency)
    df['country'] = df['country'].apply(lambda x: x.alpha3_code)
    df['trade_date'] = df['trade_year'].apply(lambda x: f"{x}-01-01")

    print(df)
