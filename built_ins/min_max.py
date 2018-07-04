nums = [40, 34, 5, 6, 10]
max(nums)  # 40
min(nums)  # 5

max('hello world')  # 'w'
min('hello world')  # ' '
max((3, 5, 23, 65))  # 65

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

min(names)  # 'Arya'
max(names)  # 'Tim'

min(len(name) for name in names)  # 3

# (len(name) for name in names) <~~ Generator Object
[len(name) for name in names]  # [4, 6, 4, 3, 10]

max_ = max(names, key=lambda n: len(n))
min_ = min(names, key=lambda n: len(n))

print(max_)  # 'Ollivander'
print(min_)  # 'Tim'

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},
]

worst_song = min(songs, key=lambda s: s['playcount'])
print(worst_song['title'])

worst_song = min(songs, key=lambda s: s['playcount'])['title']
print(worst_song)
