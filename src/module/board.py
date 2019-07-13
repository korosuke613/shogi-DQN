import shogi


class Board:
    def __init__(self):
        self.board = shogi.Board()
    
    def print(self):
        print(self.board.kif_str())
    
    def is_checkmate(self):
        self.board.is_checkmate()
