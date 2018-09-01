# Let's define a speed_test decorator
from functools import wraps
from time import time
import numpy as np

size = 10000000

gen = (x for x in range(size))
list_ = [x for x in range(size)]
numpy_ar = np.array([x for x in range(size)])


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(size))


@speed_test
def sum_nums_list():
    return sum([x for x in range(size)])


@speed_test
def sum_nums_numpy():
    return sum(np.array([x for x in range(size)]))


@speed_test
def sum_with_prebuilt(val):
    return sum(val)


print('=================================')
print('     10,000,000 iterations')
print('=================================')
print(type(gen))
sum_nums_gen()
print('---------------------------------')
sum_with_prebuilt(gen)
print('=================================')
print(type(list_))
sum_nums_list()
print('---------------------------------')
sum_with_prebuilt(list_)
print('=================================')
print(type(numpy_ar))
sum_nums_numpy()
print('---------------------------------')
sum_with_prebuilt(numpy_ar)
print('=================================')
