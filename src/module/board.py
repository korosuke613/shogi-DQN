import shogi
from .usi import Usi


class Board:
    def __init__(self):
        self.board = shogi.Board()
    
    def print(self):
        print(self.board.kif_str())
    
    def is_checkmate(self):
        return self.board.is_checkmate()

    def was_suicide(self):
        return self.board.was_suicide()

    def is_correct_usi(self, usi_original, color):
        usi = Usi(usi_original)
        attackers = self.board.attackers(color, usi.to_point_num)
        if usi.from_point_num in attackers:
            return True
        return False

    def move_piece(self, usi):
        self.board.push(shogi.Move.from_usi(usi))
