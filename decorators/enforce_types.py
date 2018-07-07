def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


print(repeat_msg("hello", '3'))


@enforce(float, float)
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide('1', '4'))
