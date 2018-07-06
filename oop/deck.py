from card import Card
import random


class Deck(object):
    def __init__(self):
        self._cards = []
        self._SIZE_OF_DECK = 52
        # self._count = len(self._cards)

    def __repr__(self):
        return f"Deck of {self.num_cards()} cards."

    def __iter__(self):
        # return iter(self._cards)
        for card in self._cards:
            yield card

    def deal(self, Player):
        dealt = self._cards.pop()
        Player._hand.append(dealt)
        return self

    def build(self):
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'jack', 'queen', 'king', 'ace')

        for suit in suits:
            for val in range(0, 13):
                new_card = Card(suit, val, ranks[val])
                self._cards.append(new_card)

        return self

    def shuffle(self):
        random.shuffle(self._cards)
        return self

    def print_self(self):
        for c in self._cards:
            c.read_card()
        return self

    def num_cards(self):
        return len(self._cards)


d = Deck()
print(d)
d.build()
print(d)
for card in d:
    print(card)
