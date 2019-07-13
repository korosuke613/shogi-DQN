from dataclasses import dataclass


@dataclass
class Player:
    name: str
    color: any
    holding_pieces: list = None
