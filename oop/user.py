class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"


user1 = User('Chuck', 'Norris', 35)
user2 = User('Blanca', 'Day', 43)
print(user1.first)
print(user1.last)
print(user2.full_name())
