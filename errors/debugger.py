# Using Python DeBugger (aka pdb)

first = "First"
second = "Second"
# pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

'''
Common PDB Commands:
--------------------

a (all variables)
l (list)
n (next line)
p (print)
c (continue - finishes debugging)

'''


def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()

    return a + b + c + d


add_numbers(1, 2, 3, 4)
