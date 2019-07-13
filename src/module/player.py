import dataclasses


@dataclasses.dataclass
class Player:
    name: str
    holding_pieces: list = None
