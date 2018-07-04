nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7, 8, 9, 10]
x = zip(nums1, nums2)
print(x)

x2 = (list(x))
print(x2)

z = dict(zip(nums1, nums2))
print(z)

y = set(x2)
print(y)

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
balls = list(zip(*five_by_two))
print(balls)

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

crazy = dict(
            zip(
                students,
                map(
                    lambda pair: max(pair),
                    zip(midterms, finals)
                )
            )
        )

print(crazy)


average = dict(
            zip(
                students,
                map(
                    lambda pair: ((pair[0] + pair[1])/2),
                    zip(midterms, finals)
                )
            )
        )

print(average)


# Exercises
def interleave(str1, str2):
    return ''.join([''.join(tup) for tup in (zip(str1, str2))])


print(interleave('hi', 'ha'))


def triple_and_filter(nums):
    return [num * 3 for num in nums if num % 4 is 0][0]


def triple_and_filter2(nums):
    return list(filter(lambda x: x % 4 is 0, map(lambda x: x*3, nums)))


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter2([1, 2, 3, 4]))


def extract_full_name(names):
    return [''.join((name['first'], name['last'])) for name in names]


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))
