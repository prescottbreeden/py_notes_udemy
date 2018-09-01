import re


def parse_name(input):
    NAME_REGEX = re.compile(
        r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = NAME_REGEX.search(input)
    print(matches.group())
    print(matches.group('first'))
    print(matches.group('last'))


parse_name("Mrs. Tilda Swinton")
