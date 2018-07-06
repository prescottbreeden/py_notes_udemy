from functools import wraps
# Wraps preserves a function's metadata when it is decorated


def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwards):
        '''I am a wrapper function'''
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwards)
    return wrapper


@log_function_data
def add(x, y):
    '''Adds two numbers together.'''
    return x + y


print(add(10, 30))


def say_hi():
    '''Says hello'''
    return "hi"


print(say_hi.__doc__)
print(add.__doc__)
print(add.__name__)
help(add)
