from game import Game
from card import Card
import random


class Deck(object):
    def __init__(self):
        self._cards = []
        self._SIZE_OF_DECK = 52
        self._count = len(self._cards)

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
        for c in deck._cards:
            c.read_card()
        return self


game1 = Game()
game1.create_players('Ricky', 'Bobby', 'Texas', 'Ranger')
deck = Deck()
deck.build().print_self().shuffle().print_self()

print(deck._count)

for p in Game.players:
    deck.deal(p)

print(deck._count)
