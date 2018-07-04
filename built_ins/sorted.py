users = [
    {"username": "samuel", "tweets": ["I love cake", "I love puppies"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

result = sorted(users, key=len)
result = sorted(users, key=lambda user: user['username'])
result = sorted(users, key=lambda user: len(user['tweets']))
result = sorted(users, key=lambda user: len(user['tweets']), reverse=True)

print(result)

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},
]

most_played = sorted(songs, key=lambda s: s['playcount'], reverse=True)

print(most_played)
