'''
*args

gathers remaining arguments as a tuple

it is jut a parameter, you can call it whatever you want
'''


def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(4, 6, 9, 4, 10))


def star(*args):
    print(args)


test = "Hello World"
test2 = test.split(' ')
star(test)

'''
**kwargs

gathers remaining keyword arguments as a dictionary

'''


def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f'{person}\'s favorite color is {color}')


fav_colors(colt="purple", ruby="red", ethel="teal")
