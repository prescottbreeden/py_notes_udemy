class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Fish(Animal):
    pass


d = Dog()
c = Cat()
f = Fish()

print(d.speak())
print(c.speak())
print(f.speak())
