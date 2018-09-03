def two_oldest_ages(ages):
    max_ages = [0, 0]
    for age in ages:
        for index, max_age in enumerate(max_ages):
            if age > max_age:
                max_ages[index] = age
                break
    max_ages.sort()
    return max_ages


print(two_oldest_ages([0, 1, 9, 10, 4]))
