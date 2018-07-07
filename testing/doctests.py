def add(x, y):
    """add together x and y

    >>> add(1, 2)
    3

    >>> add(8, 'hi')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """

    return x + y


def double(values):
    ''' double the values in a list

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    '''

    return [val * 2 for val in values]


def say_hi():
    '''
    >>> say_hi()
    'hi'

    '''
    return 'hi'


def true_that():
    '''
    >>> true_that()
    True
    '''
    return True


# order to a dictionary matters for a doc test
def make_dict(keys):
    '''
    >>> make_dict(['a', 'b'])
    {'a': True, 'b': True}
    '''
    return {key: True for key in keys}
