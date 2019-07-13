import shogi


class Board:
    def __init__(self):
        self.board = shogi.Board()
    
    def print(self):
        print(self.board.kif_str())
    
    def is_checkmate(self):
        self.board.is_checkmate()

    @staticmethod
    def convert_alphabet(alphabet):
        alphabet_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}
        return alphabet_dict[alphabet]

    def is_correct_usi(self, usi, color):
        def convert_usi2num(_usi):
            return (9 - int(_usi[0])) + (self.convert_alphabet(_usi[1]) - 1) * 9
        # usi = '7g7f'
        from_usi = usi[:2]  # 7g
        from_usi_num = convert_usi2num(from_usi)
        to_usi = usi[2:4]   # 7f
        to_usi_num = convert_usi2num(to_usi)
        attackers = self.board.attackers(color, to_usi_num)
        if from_usi_num in attackers:
            return True
        return False

    def move_piece(self, usi):
        self.board.push(shogi.Move.from_usi(usi))
