def sum_all_nums(*args):
    '''
    Accepts any number of integers and sums them

    >>> sum_all_nums(4, 6, 9, 4, 10)
    33
    '''
    return sum(arg for arg in args)

# print(sum_all_nums(4, 6, 9, 4, 10))


def star(*args):
    print(args)


# test = "Hello World"
# test2 = test.split(' ')
# star(test)


def fav_colors(**kwargs):
    '''
    Accepts any number of keyword arguments and returns a string
    with the key and the value printed as:
        "{kwarg}'s favorite color is {color}'"

    >>> fav_colors(colt="purple", ruby="red", ethel="teal")
    colt's favorite color is purple
    ruby's favorite color is red
    ethel's favorite color is teal
    '''
    for person, color in kwargs.items():
        print(f'{person}\'s favorite color is {color}')
