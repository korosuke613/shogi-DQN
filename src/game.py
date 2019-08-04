from board import Board
from player import Player
import shogi


class Game:
    """Game control Shogi."""
    def __init__(self, names):
        self.board = Board()
        colors = [shogi.BLACK, shogi.WHITE]
        self.players = [Player(name=names[i], color=colors[i]) for i in range(2)]
        self.now_player_index = 0

    def change_next_player(self):
        if self.now_player_index == 0:
            self.now_player_index = 1
        else:
            self.now_player_index = 0

    def get_now_player(self):
        """get now player
        
        Returns:
            Player -- now player
        """
        return self.players[self.now_player_index]

    def listen_usi(self):
        while True:
            usi = input()
            if self.board.is_correct_usi(usi, self.get_now_player().color):
                return usi
            else:
                print("Don't correct usi!")

    def start(self):
        """start game
        """
        while True:
            self.board.print()
            print()
            print(f'>> Turn is {self.get_now_player().name}')
            usi = self.listen_usi()
            self.board.move_piece(usi)

            if self.board.is_checkmate() is True or self.board.was_suicide() is True:
                if self.board.was_suicide() is True:
                    self.change_next_player()
                print()
                print(f'WINNER is {self.get_now_player().name}')
                return
            self.change_next_player()
