from player import Player


class Game(object):
    def __init__(self):
        self.players = []
        self.game_round = 0

    def create_players(self, *args):
        self.players = [Player(arg) for arg in args]
        return self
