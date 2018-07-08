import re

text = 'Last night Mrs. Daisy and Mr. White murdered Mr. Chow'

PATTERN = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+', re.I)
result = PATTERN.sub('**REDACTED**', text)
print(result)

result2 = PATTERN.sub('\g<1> REDACTED', text)
print(result2)

REG = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result3 = REG.sub('\g<1> \g<2>', text)
print(result3)
