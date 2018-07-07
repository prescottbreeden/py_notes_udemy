def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive."
    return x + y


# print(add_positive_numbers(1, 1))
# print(add_positive_numbers(1, -1))


def eat_junk(food):
    assert food in [
        'pizza',
        'ice cream',
        'candy',
        'fried butter'], 'food must be a junk food'
    return f"nom nom nom I am eating {food}"


food = input("Enter a food please: ")
print(eat_junk(food))

# python3 -O assert.py <~~ ignores all asserts
