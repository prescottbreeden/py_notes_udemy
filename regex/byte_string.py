import re
REGEX = re.compile(r'\b[0-1]{8}\b')


def parse_bytes(str):
    return REGEX.findall(str)
