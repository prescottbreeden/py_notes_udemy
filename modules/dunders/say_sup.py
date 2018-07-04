def say_sup():
    print(f"Sup! My __name__ is {__name__}")


if __name__ == "__main__":
    say_sup()

'''
say sup() will only be executed if the say_sup.py file is being run
because if it is being run, then the name of the file will be __main__
and thus will execute, otherwise it will read the file on import but
otherwise not execute
'''
