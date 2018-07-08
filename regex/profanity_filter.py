import re


def censor(input):
    REG = re.compile(r'\bfrack*[a-z]+\b', re.I)
    return REG.sub('CENSORED', input)


print(censor('Frack you'))
print(censor('I hope you fracking trip'))
print(censor('you fracking Frack'))
