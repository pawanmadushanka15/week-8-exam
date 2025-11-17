from datetime import date
import pytest
from seasons import minutes_between, words_for_minutes


def test_minutes_between_one_year_non_leap():
    assert minutes_between(date(1999, 1, 1), date(2000, 1, 1)) == 365 * 24 * 60


def test_minutes_between_leap_period():
    assert minutes_between(date(2019, 3, 1), date(2020, 3, 1)) == 366 * 24 * 60


def test_minutes_between_two_years_with_leap():
    assert minutes_between(date(2001, 1, 1), date(2003, 1, 1)) == (365 + 365) * 24 * 60
    assert minutes_between(date(1999, 1, 1), date(2001, 1, 1)) == (365 + 366) * 24 * 60


def test_minutes_between_future_raises():
    with pytest.raises(ValueError):
        minutes_between(date(3000, 1, 1), date(2000, 1, 1))


def test_minutes_between_type_error():
    with pytest.raises(TypeError):
        minutes_between("2000-01-01", date(2001, 1, 1))
    with pytest.raises(TypeError):
        minutes_between(date(2000, 1, 1), "2001-01-01")


def test_words_for_minutes_examples():
    # Expected strings DO NOT end with a period
    assert words_for_minutes(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert words_for_minutes(527040) == "Five hundred twenty-seven thousand, forty minutes"
    assert words_for_minutes(1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert words_for_minutes(1) == "One minutes"


def test_words_for_minutes_whitespace_and_and_removal():
    out = words_for_minutes(101)
    assert " and " not in out
    assert "  " not in out
