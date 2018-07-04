class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50

    def __chucknorris__(self):
        print('Hadooooooken!')


x = SpecialList([1, 2, 3])
print(SpecialList)
print('len: ', len(x))

x.__chucknorris__()
