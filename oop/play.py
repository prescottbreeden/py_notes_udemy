from game import Game
from deck import Deck


new_game = Game()
new_game.create_players('Ricky', 'Bobby', 'Texas', 'Ranger')
current_deck = Deck()
current_deck.build().shuffle()

print(current_deck.num_cards())

for i in range(0, new_game.hand_size):
    for p in new_game.players:
        current_deck.deal(p)

print(current_deck.num_cards())
