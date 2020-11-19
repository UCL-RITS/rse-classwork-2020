from times import time_range, compute_overlap_time
from pytest import raises
import pytest

@pytest.mark.parametrize("large, short, expected", 
                        [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')])
                        , (time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00"), [])
                        , (time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 2, 0), time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 0), [('2010-01-12 11:00:00', '2010-01-12 11:30:00'), ('2010-01-12 11:30:00', '2010-01-12 12:00:00')])
                        ,(time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 2, 0), time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00", 2, 0), [])
                        ,(time_range("2010-01-12 13:00:00", "2010-01-12 12:00:00", 4, 60), time_range("2010-01-12 14:30:00", "2010-01-12 12:00:00", 2, 60), [])
                        ])

def test_given_input(large, short,expected):
    # large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    # short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    # expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap(large, short,expected):
    # large = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    # short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    # expected = []
    assert result == expected

def test_contain_intervals(large, short,expected):
    # large = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 2, 0)
    # short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 0)
    result = compute_overlap_time(large, short)
    # expected = [('2010-01-12 11:00:00', '2010-01-12 11:30:00'), ('2010-01-12 11:30:00', '2010-01-12 12:00:00')]
    assert result == expected

def test_touching_times(large, short,expected):
    # large = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 2, 0)
    # short = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00", 2, 0)
    result = compute_overlap_time(large, short)
    # expected = []
    assert result == expected

def test_backfoward_date(large,short,expected):
    # large = time_range("2010-01-12 13:00:00", "2010-01-12 12:00:00", 4, 60)
    # short = time_range("2010-01-12 14:30:00", "2010-01-12 12:00:00", 2, 60)
    with raises(ValueError):
        compute_overlap_time(large, short)