x = [1, 2, 3, 4, 5]

evens = list(filter(lambda x: x % 2 is 0, x))
print(evens)

evens2 = [num for num in x if num % 2 is 0]
print(evens2)

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love puppies"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

inactive_users = list(filter(lambda u: len(u['tweets']) is 0, users))
print(inactive_users)

inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2)

active_users = list(filter(lambda u: any(u['tweets']), users))
print(active_users)

names = list(map(lambda user: user['username'].upper(),
                 filter(lambda u: not u['tweets'], users)))
print(names)

names2 = [user['username'].upper() for user in users if not user['tweets']]
print(names2)

names = ['Lassie', 'Colt', 'Rusty']
instructors = list(map(lambda name: f'Your instructor is {name}',
                       filter(lambda value: len(value) < 5, names)))
print(instructors)

lazy_instructors = ([f'Your instructor is {name}'
                    for name in names if len(name) < 5])
print(lazy_instructors)
