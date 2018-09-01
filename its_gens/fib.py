import sys


def fib_list(max):
    arr = []
    print(type(arr))
    a, b = 0, 1
    while len(arr) < max:
        arr.append(b)
        a, b = b, a + b
    return arr[-1]


def fib_gen(max, all=True):
    a = 0
    b = 1
    count = 0
    if all:
        while count < max:
            a, b = b, a + b
            yield b
            count += 1
    else:
        while count < max:
            a, b = b, a + b
            count += 1
        yield a


print(fib_list(10000))

# for n in fib_gen(100000, False):
    # print(n)
