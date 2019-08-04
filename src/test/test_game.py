import io

import pytest
import sys

from game import Game
from player import Player
from usi import Usi


@pytest.fixture
def game():
    return Game(["a", "b"])


def test_change_next_player(game):
    assert game.now_player_index == 0
    game.change_next_player()
    assert game.now_player_index == 1
    game.change_next_player()
    assert game.now_player_index == 0


def test_get_now_player(game):
    a = Player("a", 0)
    assert game.get_now_player() == a


def test_listen_usi_success(monkeypatch, game):
    usi = '7g7f'
    monkeypatch.setattr('sys.stdin', io.StringIO(usi))
    output = game.listen_usi()
    assert output == usi


def test_listen_usi_failed(capfd, monkeypatch, game):
    failed_usi = '7777'
    monkeypatch.setattr('sys.stdin', io.StringIO(failed_usi))
    game.listen_usi(is_test=True)
    out, err = capfd.readouterr()
    assert out == "Don't correct usi!\n"
