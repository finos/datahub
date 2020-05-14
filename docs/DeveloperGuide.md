---
id: developer
title: Developer Guide
---

The following guide give you a deeper dive about the structure of DataHub source code and its design philosophy, and explain how to customize DataHub by adding your own generator.

- [Source code structure](#source-code-strcture)
- [Setup local development environment](#setup-local-development-environment)
- [Add your own generator](#add-your-own-generator)
- [Add your own model](#add-your-own-model)

## <a name="source-code-strcture"></a>Source code structure

The major functionality of DataHub sits in the folder datahub_core with the following structure:

``` bash
├── data/
├── datasets/
├── generators/
│   ├── attribute_generators/
│   ├── data_frame/
│   ├── generate.py
│   ├── ...
├── libs/
├── models
│   ├── markov/
│   ├── sklearn/
├── ...
```

* **data**: This folder contains all the data required by different generators.
* **dataset**: This folder contains all the model definition for different generators.
* **generators**: This folder contains the generators to generate different kind of synthetic data.
* **libs**: This folder contains some shared dependency.
* **models**: This folder contains different data models, based on which DataHubcan generate synthetic data. It's an enhanced functionality to stand alone data generators. For now, we only support two models: markov and sklearn.

## <a name="setup-local-development-environment"></a>Setup local development environment

1. Setup pip.ini to enable downloading packages via company proxy(optional)
2. Install dependencies

### Setup the PIP.ini

If you are working behind a corporate firewall you may have a pypi mirror or
need to configure pip with your corporate firewall's settings. There are many resources
on stackoverflow how do to this - but essentially you need to set the index and index-url
to whatever you have setup internally

### Create a python Virtual Env

``` shell
  python3 -m venv env
  .env/scripts/Activate.bat
```

Install dependencie via PIP

``` shell
  pip install -r requirements.txt
```

Running the tests to check everything is ok

``` shell
  pytest
```

## <a name="add-your-own-generator"></a>Add your own generator

A DataHubgenerator is the key component for you to generate synthetic data based on predfined logic. Adding a new generator to DataHubis relative simple and consists of two pieces: functional wrapper and generation logic.

### Functional wrapper:

The functional wrapper of a generator provide a function which will return a function pointer with partial parameters assgined to it. You can use the below template with some pseudocode.

```python
import functools
import numpy as np

def generator_name(data, param1=None, param2=None, ...):
    """

    Embedded document here

    # Arguments:

    # Example:

    """
    return functools.partial(
        __generator_name,
        data=data,
        param1=param1,
        param2=param2,
        ...
    )

def __generator_name(data, param1=None, param2=None, ...):
    """

    Real generation logic, and you only need to return a single item from this function.

    It's recommended to wrap your generation logic to a seperate attribute generator.

    # Example:
    def __generator_name(data, param1=None, param2=None, ...):
        generator = AttributeGenerator(...)
        return generator.make(...)

    """
    return synthetic_item
```

After you create your own generator wrapper, you can put it under folder **datahub_core/generator**.

### Attribute generator:

As mentioned in above section, the recommended practice is to split your generation logic into a seperated attribute generator. You can use below template with pseudocode as an example.

```python
class YourAttributeGenerator:

    def __init__(self, ...):
        ...

    def make(self, ...):
        """

        Real generation logic here.
        
        """
        return synthetic_item
```

The file naming convension for attribute generator is **your_attribute_name**_generator.py, and place that file under folder **datahub_core/generators/attribute_generators**.

## <a name="add-your-own-model"></a>Add your own model

A DataHubmodel is an advanced way to generate your synthetic data based on some statistic features of your input data or some predefined relations between different columns compared to the relative simple way to generate synthetic data based on a single generator.

The way to define a new model is relatively simple, please refer to the below template with pseudocode.

```python
class YourModel:
    def __init__(self, filename, xfields, yfields):
        ...

    # optional
    def set_precondition(self, data):
        ...

    def make_one(self):
        return synthetic_item
```

The model also has a relative simple interface, and you only need to return a single item from *make_one* interface. The *set_precondition* interface is optional, and only need to implement when your model has any dependent data.
