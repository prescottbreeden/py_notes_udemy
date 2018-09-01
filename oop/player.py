class Player(object):
    def __init__(self, name):
        self.name = name
        self._hand = []
        self.tokens = 3

    def show_hand(self):
        for c in self._hand:
            print(c)
