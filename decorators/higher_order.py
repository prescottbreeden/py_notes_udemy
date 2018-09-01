# We can pass funcs as args to other funcs
def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x*x


def cube(x):
    return x*x*x


print(sum(10, square))
print(sum(3, square))
print(sum(3, cube))
