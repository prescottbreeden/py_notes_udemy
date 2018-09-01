class Card(object):
    def __init__(self, suit, value, rank):
        self._suit = suit
        self._value = value
        self._rank = rank

    def read_card(self):
        print(f"{self._rank} of {self._suit}")


# card = Card('spades', 14, 'Ace')
# card.read_card()
