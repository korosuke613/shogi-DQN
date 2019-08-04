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


def test_start(game, capfd):
    def listen_usi_generator():
        for l in ["7g7f", "3c3d"]:
            yield l

    def listen_usi_mock():
        return listen_usi.__next__()

    listen_usi = listen_usi_generator()
    game.listen_usi = listen_usi_mock

    try:
        game.start()
    except StopIteration:
        out, err = capfd.readouterr()
        game.board.print()
        out, err = capfd.readouterr()
        assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
|v香v桂v銀v金v玉v金v銀v桂v香|一
| ・v飛 ・ ・ ・ ・ ・v角 ・|二
|v歩v歩v歩v歩v歩v歩 ・v歩v歩|三
| ・ ・ ・ ・ ・ ・v歩 ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ 歩 ・ ・ ・ ・ ・ ・|六
| 歩 歩 ・ 歩 歩 歩 歩 歩 歩|七
| ・ 角 ・ ・ ・ ・ ・ 飛 ・|八
| 香 桂 銀 金 玉 金 銀 桂 香|九
+---------------------------+
先手の持駒：
"""
