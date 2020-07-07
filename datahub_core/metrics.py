""" metrics functions """
import time
import inspect
import csv

CSV = csv.writer(open('./.temp/metrics.csv', 'w+', newline='\n'))

def timeit(method):
    """ Decorator to time and log function execution time"""

    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)

        end_time = time.time()
        duration = (end_time - start_time) * 1000
        method_class = get_class_that_defined_method(method)

        data = [
            method_class.__name__,
            method.__name__,
            duration,
            "ms"
        ]

        CSV.writerow(data)
        
        return result
    return timed


def get_class_that_defined_method(meth):
    """ Get the class that the method belongs to """
    if inspect.ismethod(meth):

        for cls in inspect.getmro(meth.__self__.__class__):
            if cls.__dict__.get(meth.__name__) is meth:
                return cls
    if inspect.isfunction(meth):

        return getattr(inspect.getmodule(meth),
                       meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])

    return None  # not required since None would have been implicitly returned anyway
