from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't do that!"

    def __mul__(self, other, make_copy=False):
        if isinstance(other, Human):
            return "You are multuplying humans!!"
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "what you doin bro?"


j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 49)
print(j)
print(len(j))

print(j + k)
print(j * k)

print('--------')

triplets = j * 3
triplets[1].first = 'Jessica'
print(triplets)

family = (k + j) * 3
print(family)
