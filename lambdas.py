def square(num): return num * num


print(square(9))

x = lambda num: num * num  # Don't normally store lambdas in variables
print(x(9))

x = lambda a, b: a + b
print(x(2, 8))
