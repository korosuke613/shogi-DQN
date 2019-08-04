
class Usi:
    alphabet_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}

    def __init__(self, usi):
        self.original = usi
        self.from_point = usi[:2]
        self.from_point_num = self.convert_usi2num(self.from_point)
        self.to_point = usi[2:4]
        self.to_point_num = self.convert_usi2num(self.to_point)
        self.is_upgrade = self._is_upgrade()

    def _is_upgrade(self):
        if len(self.original) != 5:
            return False
        if self.original[4] == "+":
            return True
        return False

    @classmethod
    def convert_usi2num(cls, _usi):
        return (9 - int(_usi[0])) + (cls.alphabet_dict[_usi[1]] - 1) * 9
