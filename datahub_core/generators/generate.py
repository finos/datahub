#pylint:disable=line-too-long
import multiprocessing
import numpy as np
from joblib import Parallel, delayed
from . import ResultObject
from . import Context
from ..models import NoneModel
from ..models import MarkovModel

def generate_from_model(props, model=NoneModel(), count=50, randomstate=np.random):
    """
    Generate with a model, the model is called first to populate the object,
    the pops parameter is used to populate the rest of the object
    """
    results = []
    context = Context(count)

    for _ in range(0, count):

        result = generate_from_model_single(props, context, model, randomstate)
        results.append(result)

    return ResultObject(results)

def generate_from_model_single(props, context, model=NoneModel(), randomstate=np.random):
    result = {}

    # check if a model has any pre-condition
    pre_condition_flag = callable(getattr(model, "set_precondition", None))

    if not pre_condition_flag:
        result.update(model.make_one())

    for k, v in props.items():
        x = v(df=result, key=k, context=context, randomstate=randomstate)
        result[k] = x

    if pre_condition_flag:
        model.set_precondition(result)
        result.update(model.make_one())

    return result

def generate_from_model_parallel(props, context, model=NoneModel(), count=50, randomstate=np.random):
    num_cores = multiprocessing.cpu_count()
    results = Parallel(n_jobs=num_cores)(delayed(generate_from_model_single)(props, context, model, randomstate) for i in range(0, count))

    return ResultObject(results)

def generate(props, count=50, filename=None, randomstate=np.random):
    """
    LEGACY generate function, please use generate_from_model, if a
    filename is specified used a MarkovMode.
    """

    # Legacy, if a filename was specified it used to mean a MarkovModel
    if filename:
        return generate_from_model(
            props,
            MarkovModel(filename, randomstate),
            count,
            randomstate)

    ## No model, just generate with None
    return generate_from_model(
        props,
        NoneModel(),
        count,
        randomstate)
