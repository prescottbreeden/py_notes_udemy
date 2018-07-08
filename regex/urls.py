import re

URL_REGEX = re.compile(
    r'(https?)'  # group: "protocol"
    '://'
    '([A-Za-z]{3,10}.[A-za-z-]{2,256}\.[a-z]{2,6})'  # group: "domain"
    '([-a-zA-Z0-9@:%_\+.~#?&//=]*)'  # group: "additional info"
)

protocol_list = []
domain_list = []
info_list = []


def url_statistics(url):
    with open(url) as file:
        urls = file.readlines()
    for url in urls:
        match = URL_REGEX.search(url)
        matches = match.groups()
        protocol_list.append(matches[0])
        domain_list.append(matches[1])
        info_list.append(matches[2])


url_statistics('example_urls.txt')
print(len(protocol_list))
print(len(domain_list))
print(len(info_list))
