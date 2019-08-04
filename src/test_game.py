import pytest

from game import Game
from player import Player


@pytest.fixture
def game():
    return Game(["a", "b"])


def test_change_next_player(game):
    assert game.now_player_index == 0
    game.change_next_player()
    assert game.now_player_index == 1


def test_get_now_player(game):
    a = Player("a", 0)
    assert game.get_now_player() == a
