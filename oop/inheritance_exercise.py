# Define your classes below:
class Human:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Mother(Human):
    def __init__(self, eye_color, hair_color, hair_type):
        super().__init__(eye_color, hair_color, hair_type)


class Father(Human):
    def __init__(self, eye_color, hair_color, hair_type):
        super().__init__(eye_color, hair_color, hair_type)


class Child(Mother, Father):
    def __init__(self, eye_color, hair_color, hair_type):
        super().__init__(eye_color, hair_color, hair_type)


mother = Mother('brown', 'dark brown', 'curly')
father = Father('blue', 'blond', 'straight')
child = Child('orange', 'green', 'spikey')

print(mother.eye_color)
print(father.eye_color)
print(child.eye_color)
