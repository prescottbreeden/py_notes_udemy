def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


print(count_up_to(5))
counter = count_up_to(5)


def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
    for day in days:
        yield day


days = week()
print(next(days))
print(next(counter))
print(next(days))
print(next(days))
print(next(counter))
print(next(days))
print(next(days))
print(next(days))
print(next(counter))
print(next(days))
print(next(counter))
print(next(counter))
