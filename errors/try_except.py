try:
    foobar
except:
    print("You silly goosey... foobar isn't defined! but thats ok, I'll keep going...")
print("after try")

# --------------------------------

try:
    foo
except NameError:
    print("this is a name error")

# --------------------------------


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {"name": "Ricky", "last_name": "Bobby"}
print(get(d, "city"))
print(get(d, "name"))
print(get(d, "last_name"))

# --------------------------------

try:
    num = int(input("please enter a number: "))
except:
    print("That's not a number!")
else:
    print("I'm in the else because you gave me a nommy nummy")
finally:
    print("YOU SHALL NOT PASS!!!!!")

# --------------------------------

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("I'm in the else because you gave me a nommy nummy")
        break
    finally:
        print("YOU SHALL NOT PASS!!!!!")
print("Rest of game logic here....")

# --------------------------------


def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("something went wrong...")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


divide(1,'2')
