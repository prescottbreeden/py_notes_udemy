import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}\b$')
    match = phone_regex.search(input)
    if match:
        return True
    return False


def is_valid_phone2(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


print(extract_phone("my number is 206 890-8208"))
print(extract_phone("my number is 206 890-8208234"))

print(extract_all_phones(
    'my number is 555 555-5555 or call me at 555 555-5555'))
print(extract_all_phones(
    'my number is 5'))

print(is_valid_phone('555 555-5555'))
print(is_valid_phone('cell: 555 555-5555'))

print(is_valid_phone2('555 555-5555'))
print(is_valid_phone2('cell: 555 555-5555'))
