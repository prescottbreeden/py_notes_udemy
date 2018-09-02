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

# parens_valid
def valid_parentheses(str):
    num_open = 0
    for s in str:
        if num_open < 0:
            return False
        if s == '(':
            num_open += 1
        if s == ')':
            num_open -= 1
    return (num_open == 0)

#reverse vowels
def reverse_vowels(str):
    res = ''
    vowels = [s for s in str if s.lower() in 'aeiou']
    for s in str:
        if s.lower() in 'aeiou':
            res += vowels.pop()
        else:
            res += s
    return res


def three_odd_numbers(lst):
    start_idx = 0
    while(start_idx < len(lst)-2):
        idx = 0
        sum = 0
        while(idx < 3):
            sum += lst[start_idx + idx]
            idx += 1
        if sum % 2 != 0:
            return True
        start_idx += 1
    return False


res = three_odd_numbers([1,2,3,4,5])
print(res)




