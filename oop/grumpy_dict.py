class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f'YOU WANT {key}?  WELL IT AINT HERE!')

    def __setitem__(self, key, value):
        print('YOU WANT TO CHANGE THE DICTIONARY?!')
        print('(sigh) ... FINE...')
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("No looking!... and you call yourself a programmer...")
        return False


data = GrumpyDict({'first': 'Tom', 'animal': 'cat'})
data['city'] = 'Tokyo'
print(data)
'cat' in data
