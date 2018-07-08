import re

pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
pat = re.compile(r'''
                  ^([a-z0-9_\.-]+)  # first part of email
                  @                 # single @ sign
                  ([0-9a-z\.-]+)    # email provider
                  \.                # single period
                  ([a-z\.]{2,6})$   # com, org, net, etc.
                  ''', re.VERBOSE | re.IGNORECASE)  # re.X also works


match = pat.search('chUck321@gMail.com')
print(match.group().lower())
print(match.groups())
