from day04 import (
    has_required_fields,
    in_range,
    valid_birth_year,
    valid_expiration_year,
    valid_eye_color,
    valid_hair_color,
    valid_height,
    valid_issue_year,
    valid_pid,
)

import pytest


@pytest.mark.parametrize(
    "year, expected",
    [
        (2009, False),
        (2010, True),
        (2011, True),
        (2010, True),
        (2019, True),
        (2020, True),
        (2021, False),
    ]
)
def test_valid_issue_year(year, expected):
    passport = dict(iyr=year)
    assert valid_issue_year(passport) is expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (2019, False),
        (2020, True),
        (2021, True),
        (2025, True),
        (2029, True),
        (2030, True),
        (2031, False),
    ]
)
def test_valid_expiration_year(year, expected):
    passport = dict(eyr=year)
    assert valid_expiration_year(passport) is expected

@pytest.mark.parametrize(
    "value,lower,upper,expected",
    [
        # Positive
        ("1920", 1920, 2002, True),
        ("2002", 1920, 2002, True),
        ("1981", 1920, 2002, True),
        ("1920", 1920, 2002, True),
        # Negative
        ("1880", 1920, 2002, False),
        ("1919", 1920, 2002, False),
        ("2003", 1920, 2002, False),
        ("2020", 1920, 2002, False),
        # Bad value
        ("foo", 1, 5, False),
    ],
)
def test_in_range(value, lower, upper, expected):
    assert in_range(value, lower, upper) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        # Positive
        ("150cm", True),
        ("180cm", True),
        ("193cm", True),
        ("65in", True),
        ("70in", True),
        ("76in", True),
        # Negative
        ("149cm", False),
        ("16in", False),
        ("194cm", False),
        ("64in", False),
        ("77in", False),
        ("800cm", False),
        ("80cm", False),
        ("99in", False),
        # Bad unit
        ("45km", False),
        # Not a number
        ("fivecm", False),
    ],
)
def test_valid_height(value, expected):
    passport = dict(hgt=value)
    assert valid_height(passport) is expected


@pytest.mark.parametrize(
    "keys,expected",
    [
        # Positive
        ("ecl pid eyr hcl byr iyr hgt", True),
        ("ecl pid eyr hcl byr iyr hgt cid", True),
        # Negative
        ("pid eyr hcl byr iyr hgt", False),  # Missing ecl
        ("ecl eyr hcl byr iyr hgt", False),  # Missing pid
        ("ecl pid hcl byr iyr hgt", False),  # Missing eyr
        ("ecl pid eyr byr iyr hgt", False),  # Missing hcl
        ("ecl pid eyr hcl iyr hgt", False),  # Missing byr
        ("ecl pid eyr hcl byr hgt", False),  # Missing iyr
        ("ecl pid eyr hcl byr iyr", False),  # Missing hgt
        ("ecl pid eyr hcl byr", False),  # Missing multiple
    ],
)
def test_has_required_fields(keys, expected):
    passport = dict.fromkeys(keys.split())
    assert has_required_fields(passport) is expected


@pytest.mark.parametrize(
    "color,expected",
    [
        ("#19fa3d", True),  # Positive
        ("#19FA3D", False),  # Spec said lower case only
        ("123abc", False),  # No hash
        ("#7fa", False),  # Incorrect length
    ],
)
def test_valid_hair_color(color, expected):
    passport = dict(hcl=color)
    assert valid_hair_color(passport) is expected


@pytest.mark.parametrize(
    "color,expected",
    [
        # Positive
        ("amb", True),
        ("blu", True),
        ("brn", True),
        ("gry", True),
        ("grn", True),
        ("hzl", True),
        # Negative
        ("blue", False),  # Not in list
        ("AMB", False),  # Upper case
    ],
)
def test_valid_eye_color(color, expected):
    passport = dict(ecl=color)
    assert valid_eye_color(passport) is expected


@pytest.mark.parametrize(
    "pid,expected",
    [
        ("012345678", True),
        ("012345blu", False),  # Not all digits
        ("12345", False),  # Incorrect length
    ]
)
def test_valid_pid(pid, expected):
    passport = dict(pid=pid)
    assert valid_pid(passport) is expected


@pytest.mark.parametrize(
    "byr,expected",
    [
        (1920, True), (1921, True),
        (1988, True),
        (2001, True), (2002, True),
        (1919, False), (2003, False),
    ]
)
def test_valid_birth_year(byr, expected):
    passport = dict(byr=byr)
    assert valid_birth_year(passport) is expected
