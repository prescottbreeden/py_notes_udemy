lst = [1,2,3,4,5]

for counter, value in enumerate(lst):
    print(counter, value)

fruits = ['apples', 'oranges', 'pears', 'pineapples']

for counter, value in enumerate(fruits, 0):
    print(counter, value)

for counter, value in enumerate(fruits, 1):
    print(counter, value)

'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(ages):
    max_ages = [0, 0]
    for age in ages:
        for index, max_age in enumerate(max_ages):
            if age > max_age:
                max_ages[index] = age
                break;
    max_ages.sort()
    print(max_ages)

two_oldest_ages([1,2,10,8])
two_oldest_ages([6, 1, 10, 9, 4])
two_oldest_ages([4,25,3,20,19,5]) 
