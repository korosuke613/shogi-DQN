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


def test_start_1(game, capfd):
    def listen_usi_generator():
        for l in ["7g7f", "7c7d"]:
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
|v歩v歩 ・v歩v歩v歩v歩v歩v歩|三
| ・ ・v歩 ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ 歩 ・ ・ ・ ・ ・ ・|六
| 歩 歩 ・ 歩 歩 歩 歩 歩 歩|七
| ・ 角 ・ ・ ・ ・ ・ 飛 ・|八
| 香 桂 銀 金 玉 金 銀 桂 香|九
+---------------------------+
先手の持駒：
"""


def test_start_2(game, capfd):
    def listen_usi_generator():
        for l in ["7g7f", "7c7d", "7f7e", "1c1d", "7e7d", "1d1e", "7d7c+", "1e1f", "7c6c", "1f1g", "5g5f", "1g1h+",
                  "5f5e", "1h1i", "5e5d", "1i2i", "5d5c+", "2i3i", "5c4c", "3i3h", "2h5h", "6a5b", "6c5b", "4a3b",
                  "4c5b"]:
            yield l

    def listen_usi_mock():
        return listen_usi.__next__()

    listen_usi = listen_usi_generator()
    game.listen_usi = listen_usi_mock

    game.start()
    out, err = capfd.readouterr()
    game.board.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：　銀　桂　香　歩
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
|v香v桂v銀 ・v玉 ・v銀v桂v香|一
| ・v飛 ・ ・ と ・v金v角 ・|二
|v歩v歩 ・ ・ ・ とv歩v歩 ・|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| 歩 歩 ・ 歩 ・ 歩 歩 歩 ・|七
| ・ 角 ・ ・ 飛 ・vと ・ ・|八
| 香 桂 銀 金 玉 金 ・ ・ ・|九
+---------------------------+
先手の持駒：　金　歩四
"""


if __name__ == '__main__':
    game = Game(["a", "b"])
    test_start_2(game)
