from .board import Board
from .player import Player


class Game:
    """Game control Shogi."""
    def __init__(self, names):
        self.board = Board()
        self.players = [Player(name=names[i]) for i in range(2)]
        self.now_player_index = 1

    def get_now_player(self):
        """get now player
        
        Returns:
            Player -- now player
        """
        if self.now_player_index == 0:
            self.now_player_index = 1
        else:
            self.now_player_index = 0
        return self.players[self.now_player_index]

    @staticmethod
    def listen_usi():
        return input()

    def start(self):
        """start game
        """
        while True:
            self.board.print()
            print()
            print(f'>> Turn is {self.get_now_player().name}')
            print(self.listen_usi())
