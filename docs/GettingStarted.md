---
id: home
title: Getting Started
---
The following guide gives a short introduction to the DataHub via a practical example.

## Create a python virtual env

``` bash
python -m venv env
```

## Activate the virtual environment

On macOS and Linux:

``` bash
source env/bin/activate
```

On Windows

``` bash
.\env\Scripts\activate
```

## Install datahub-core via PIP

``` bash
pip install datahub-core
```

## <a name="greate-your-first-sample-project"></a>Create your first sample project

Recommended folder structure

``` bash
├── data
│   ├── data.csv
│   ├── data.xlsx
├── project_name
│   ├── __init__.py
│   ├── generate.py
├── tests
│   ├── __init__.py
├── run.py
```

Your project's source code is mainly placed under the project_name folder. This is where your core data generation logic will be placed. run.py is a wrapper for your project entrance.

## <a name="generate-your-synthetic-data"></a>Generate your synthetic data

Once you have your folder structure prepared based on the example in the above section. You can write some code to generate your synthetic data now. There's an example in the folder **examples/demo**. The key data generation logic sit
in file **examples/demo/demo/generate.py**.

``` python
import numpy as np
import datahub_core.generators as gen

def run(seed=130319810):

    df = gen.generate(
        props={
            'region': gen.choice(data=['NAM']),
            'country': gen.country_codes(region_field='region'),
            'person_name': gen.person('country'),
            'age': gen.random_range(low=1, high=100, round_dp=0),
        },
        count=50,
        randomstate=np.random.RandomState(seed)
    ).to_dataframe()

    df['ccy'] = df['country'].apply(lambda x: x.currency)
    df['country'] = df['country'].apply(lambda x: x.alpha3_code)

    return df
```

This example generates faked person name in the NAM region with his/her country code, currency information, and random age. In order to build your own synthetic generation model, you need to define a run function, in which you will use the generators in module **datahub_core.generators** to generate your data. Both *gen.choice*, *gen.country_codes*, *gen.random_range* are the generators defined in **datahub_core/generators/data_frame**.

Enjoy your journey to the synthetic data generation now!
