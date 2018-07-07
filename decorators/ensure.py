from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed, sorry...")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")


greet("bob")
# greet(name='jerkface')

# -----------------------------


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


add_all()                   # 0
print(add_all(1, 2))        # 3
print(add_all(1, 2, 3))     # "Too many arguments!"

# -------------------------------


def ensure_only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                return ValueError("Arguments for 'add' must be integers")
        return fn(*args, **kwargs)
    return wrapper


@ensure_only_ints
def add(x, y):
    return x + y


print(add(3, 5))
print(add(2.2, 4.2))

# -------------------------------


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') is 'admin':
            return fn(*args, **args)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"


show_secrets(role="admin")  # "Shh! Don't tell anybody!"
show_secrets(role="nobody")  # "Unauthorized"
show_secrets(a="b")  # "Unauthorized"
