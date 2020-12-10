from day05 import select, select_in_range, seat_id


def test_select():
    assert select(0, 127, "F") == (0, 63)
    assert select(0, 127, "R") == (64, 127)
    assert select(70, 71, "F") == (70, 70)
    assert select(70, 71, "B") == (71, 71)

    assert select(0, 7, "L") == (0, 3)
    assert select(0, 7, "R") == (4, 7)


def test_select_row():
    assert select_in_range(0, 127, "FBFBBFF") == 44
    assert select_in_range(0, 127, "BFFFBBF") == 70
    assert select_in_range(0, 127, "FFFBBBF") == 14


def test_seat_id():
    assert seat_id("FBFBBFFRLR") == 357
    assert seat_id("BFFFBBFRRR") == 567
    assert seat_id("FFFBBBFRRR") == 119
    assert seat_id("BBFFBBFRLL") == 820
