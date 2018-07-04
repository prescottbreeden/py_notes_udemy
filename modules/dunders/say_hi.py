from say_sup import say_sup


def say_hi():
    print(f"Hi! My __name__ is {__name__}")


say_hi()
say_sup()

'''
When you import, python:
    1. Tries to find the module (if it fails, throws an error),
    2. Runs the code inside the modlue being imported,
    3.
'''
