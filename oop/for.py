# Custom For Loop
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            y = next(iterator)
        except StopIteration:
            break
        else:
            func(y)


def square(num):
    print(num*num)


name = "balls"
my_for(name, print)

arr = [1, 2, 3, 4, 5]
my_for(arr, square)
