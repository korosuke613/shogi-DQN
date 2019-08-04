from usi import Usi


def test_convert_usi2num():
    usi = Usi("4i5i+")
    assert usi.from_point == '4i'
    assert usi.from_point_num == 77
    assert usi.to_point == '5i'
    assert usi.to_point_num == 76


def test_is_upgrade():
    usi = Usi('4i5i+')
    assert usi.is_upgrade is True
