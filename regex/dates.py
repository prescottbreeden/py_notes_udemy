import re

REGEX = re.compile(
    r'^(?P<day>[0-9]{2})[/.,]*(?P<month>[0-9]{2})[/.,]*(?P<year>[0-9]{4})$')


def parse_date(input):
    matches = REGEX.search(input)
    if matches:
        return {
            'd': matches.group('day'),
            'm': matches.group('month'),
            'y': matches.group('year')
        }
    return None


x = parse_date('12,04,2003')
y = parse_date('12.11.2003')
z = parse_date('12.11.2032324')

print(x)
print(y)
print(z)
