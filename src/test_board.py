from board import Board


def test_print(capfd):
    b = Board()
    b.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
|v香v桂v銀v金v玉v金v銀v桂v香|一
| ・v飛 ・ ・ ・ ・ ・v角 ・|二
|v歩v歩v歩v歩v歩v歩v歩v歩v歩|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| 歩 歩 歩 歩 歩 歩 歩 歩 歩|七
| ・ 角 ・ ・ ・ ・ ・ 飛 ・|八
| 香 桂 銀 金 玉 金 銀 桂 香|九
+---------------------------+
先手の持駒：
"""


def test_is_correct_usi():
    b = Board()
    assert b.is_correct_usi("7g7f", 0) is True


def test_is_checkmake(capfd):
    """チェックメイトになることを確認するテスト"""
    # 黒(後手)の2手目
    b = Board("7sk/9/8+B/9/6N2/9/9/9/9 b - 2")
    b.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
| ・ ・ ・ ・ ・ ・ ・v銀v玉|一
| ・ ・ ・ ・ ・ ・ ・ ・ ・|二
| ・ ・ ・ ・ ・ ・ ・ ・ 馬|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ 桂 ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| ・ ・ ・ ・ ・ ・ ・ ・ ・|七
| ・ ・ ・ ・ ・ ・ ・ ・ ・|八
| ・ ・ ・ ・ ・ ・ ・ ・ ・|九
+---------------------------+
先手の持駒：
"""
    assert b.is_checkmate() is False
    assert b.was_suicide() is False

    # 2三桂
    assert b.is_correct_usi("3e2c", 0) is True
    b.move_piece("3e2c")
    b.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
| ・ ・ ・ ・ ・ ・ ・v銀v玉|一
| ・ ・ ・ ・ ・ ・ ・ ・ ・|二
| ・ ・ ・ ・ ・ ・ ・ 桂 馬|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| ・ ・ ・ ・ ・ ・ ・ ・ ・|七
| ・ ・ ・ ・ ・ ・ ・ ・ ・|八
| ・ ・ ・ ・ ・ ・ ・ ・ ・|九
+---------------------------+
先手の持駒：
"""
    # チェックメイト
    assert b.is_checkmate() is True
    assert b.was_suicide() is False


def test_was_suicide(capfd):
    """自殺になることを確認するテスト"""
    # b = Board("lnsg1g1nl/3k3r1/pppp1s1pp/b3p1p2/2PP1p2B/P3P3P/1P3PPP1/1S3K1R1/LN1G1GSNL w - 1")
    # 黒(後手)の2手目
    b = Board("7sk/9/9/9/6N2/9/9/9/9 b - 2")
    b.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
| ・ ・ ・ ・ ・ ・ ・v銀v玉|一
| ・ ・ ・ ・ ・ ・ ・ ・ ・|二
| ・ ・ ・ ・ ・ ・ ・ ・ ・|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ 桂 ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| ・ ・ ・ ・ ・ ・ ・ ・ ・|七
| ・ ・ ・ ・ ・ ・ ・ ・ ・|八
| ・ ・ ・ ・ ・ ・ ・ ・ ・|九
+---------------------------+
先手の持駒：
"""
    assert b.is_checkmate() is False
    assert b.was_suicide() is False

    # 2三桂
    assert b.is_correct_usi("3e2c", 0) is True
    b.move_piece("3e2c")
    b.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
| ・ ・ ・ ・ ・ ・ ・v銀v玉|一
| ・ ・ ・ ・ ・ ・ ・ ・ ・|二
| ・ ・ ・ ・ ・ ・ ・ 桂 ・|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| ・ ・ ・ ・ ・ ・ ・ ・ ・|七
| ・ ・ ・ ・ ・ ・ ・ ・ ・|八
| ・ ・ ・ ・ ・ ・ ・ ・ ・|九
+---------------------------+
先手の持駒：
"""
    # チェックメイトじゃない
    assert b.is_checkmate() is False
    assert b.was_suicide() is False

    # 2二銀
    assert b.is_correct_usi("2a2b", 1) is True
    b.move_piece("2a2b")
    b.print()
    out, err = capfd.readouterr()
    assert out == """後手の持駒：
  ９ ８ ７ ６ ５ ４ ３ ２ １
+---------------------------+
| ・ ・ ・ ・ ・ ・ ・ ・v玉|一
| ・ ・ ・ ・ ・ ・ ・v銀 ・|二
| ・ ・ ・ ・ ・ ・ ・ 桂 ・|三
| ・ ・ ・ ・ ・ ・ ・ ・ ・|四
| ・ ・ ・ ・ ・ ・ ・ ・ ・|五
| ・ ・ ・ ・ ・ ・ ・ ・ ・|六
| ・ ・ ・ ・ ・ ・ ・ ・ ・|七
| ・ ・ ・ ・ ・ ・ ・ ・ ・|八
| ・ ・ ・ ・ ・ ・ ・ ・ ・|九
+---------------------------+
先手の持駒：
"""
    assert b.is_checkmate() is False
    assert b.was_suicide() is True
