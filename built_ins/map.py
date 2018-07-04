nums = [2, 4, 6, 8, 10]
balls = list(map(lambda x: x*2, nums))
print(balls)

x = [num * 2 for num in nums]
print(x)

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)


def decrement_list(nums):
    return list(map(lambda x: x-1, nums))


print(decrement_list([1, 2, 3, 4, 5]))
