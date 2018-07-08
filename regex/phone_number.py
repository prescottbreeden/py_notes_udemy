import re

# Define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# Search a string with our regex
res = pattern.search('Call me at 415 555-4242!')

print(res)
