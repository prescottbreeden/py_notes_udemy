# A User class with both instance attributes and instance methods
class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, dat_str):
        first, last, age = dat_str.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}, {self.first}"


# print(User.active_users)
# user1 = User('Chuck', 'Norris', 35)
# user2 = User('Blanca', 'Day', 43)
# print(user1.first)
# print(user1.last)
# print(user2.full_name())
# print(User.active_users)
# print(user2.logout())
# print(User.active_users)

# print(User.display_active_users())
chuck = User.from_string('chuck,norris,35')
print(User.display_active_users())
print(chuck.first, chuck.last, chuck.age)
print(type(chuck.age))
