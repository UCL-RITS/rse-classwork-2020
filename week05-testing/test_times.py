from times import compute_overlap_time, time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

    large2 = time_range("2008-01-12 10:00:00", "2010-01-12 12:00:00")
    short2 = time_range("2008-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large2,short2)
    expected = [('2008-01-12 10:30:00', '2009-01-11 22:37:00'), ('2009-01-11 22:38:00', '2010-01-12 10:45:00')]
    assert result == expected

    large3 = time_range("2010/01/12 10:00:00", "2010-01-12 12:00:00")
    short3 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large3,short3)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


