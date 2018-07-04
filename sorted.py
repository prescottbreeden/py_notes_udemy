users = [
    {"username": "samuel", "tweets": ["I love cake", "I love puppies"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

# print(sorted(users, key=len))
# print(sorted(users, key=lambda user: user['username']))
print(sorted(users, key=lambda user: len(user['tweets'])))
