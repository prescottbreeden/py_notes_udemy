'''
Compact

Write a function called compact that accepts a list and returns a list of
values that are truthy values, without any of the falsey value
'''


def compact(ar):

    truthy = []
    for val in ar:
        if val:
            truthy.append(val)
        else:
            continue

    print(truthy)
    return truthy


compact([0, 1, 2, "", [], False, {}, None, "All done"])

# [1,2, "All done"]

'''
Intersection

Write a function called intersection that accepts two lists and returns
a list with the values that in both input lists
'''


def intersection(x, y):
    return [value for value in x if value in y]


def intersectionSetVersion(x, y):
    return [val for val in set(x) & set(y)]


x = [1, 2, 3, 4, 5, 6, 7]
y = [4, 2, 9, 1, 3, 4, 5, 23, 6]
print(intersectionSetVersion(x, y))

'''
Partition

Accept a list and a callback function (which you can assume
return True or False)  The function should iterate over each element in the
list and invoke the callback function at each iteration.

if the callback is true, element should go inot the first list
if the callback is false, element should go into the second tlist

should return [truthy_list, falsy_list]
'''


def partition(ar, fx):
    truthy_list = []
    falsy_list = []
    for val in ar:
        if(fx(val)):
            truthy_list.append(val)
        else:
            falsy_list.append(val)

    result = [truthy_list, falsy_list]
    print(result)
    return result


def partitionLI(lst, fn):
    x = [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
    return x


def isEven(num):
    return num % 2 == 0


partitionLI([1, 2, 3, 4], isEven)
