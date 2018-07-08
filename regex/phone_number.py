import re

# Define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# Search a string with our regex
res = pattern.search('Call me at 415 555-4242!')
print(res)
print(res.group)

res = pattern.findall('call me at 310 445-9876 or 310 234-9999')
print(res)

# below is expensive if used repeatedly, compiles each time thi way
print(re.search(r'\d{3} \d{3}-\d{4}', 'call me at 310 445-9876'))
print(re.search(r'\d{3} \d{3}-\d{4}', 'call me at 310 445-9876').group)
