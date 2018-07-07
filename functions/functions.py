def compact(ar):
    '''
    Accepts a list and returns a new list of values that are truthy values,
    without any of the falsey value

    >>> compact([1, 2, 3, 4])
    [1, 2, 3, 4]

    >>> compact([True, False, 0, None, ''])
    [True]
    '''
    truthy = []
    for val in ar:
        if val:
            truthy.append(val)
        else:
            continue

    return truthy


# compact([0, 1, 2, "", [], False, {}, None, "All done"])

# [1,2, "All done"]


def intersection(x, y):
    '''
    Accepts two lists and returns a list with the values
    that are in both lists

    >>> intersection([1, 2, 3], [2, 3, 4])
    [2, 3]

    >>> intersection([1, 2, 3], [4, 5, 6])
    []

    >>> intersection(['1', '2', '3'], ['1', 'bob', '3'])
    ['1', '3']

    '''
    return [value for value in x if value in y]


def intersectionSetVersion(x, y):
    return [val for val in set(x) & set(y)]


# x = [1, 2, 3, 4, 5, 6, 7]
# y = [4, 2, 9, 1, 3, 4, 5, 23, 6]
# print(intersectionSetVersion(x, y))


def partition(ar, fn):
    '''
    Accept a list and a callback function which return True or False.
    The function should iterate over each element in the
    list and invoke the callback function at each iteration.

    if the callback is true, element should go inot the first list
    if the callback is false, element should go into the second tlist

    pseudo expected output: [truthy_list, falsy_list]

    >>> partition([1, 2, 3, 4], isEven)
    [[2, 4], [1, 3]]

    >>> partition(['1', '2', '3', '4'], isEven)
    Traceback (most recent call last):
        ...
    TypeError: not all arguments converted during string formatting

    '''
    x = [[val for val in ar if fn(val)], [val for val in ar if not fn(val)]]
    return x


def isEven(num):
    return num % 2 == 0


# partitionLI([1, 2, 3, 4], isEven)
