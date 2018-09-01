# Titleize

def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


# find_factors

def find_factors(num):
    factors = []
    i = 1
    while(i <= num):
        if (num % i == 0):
            factors.append(i)
        i += 1
    return factors


# includes

def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]


# repeat

def repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr


# truncate

def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string
 
    return string[:n - 3] + "..."

# sum_up_diagonals

def sum_up_diagonals(arr):
    total = 0

    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total
# min_max_key_in_dictionary

def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]
# find_greater_numbers

def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count;


# two_oldest

def two_oldest_ages(ages):
    return sorted(ages)[-2:]
# is_odd_string

def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1
