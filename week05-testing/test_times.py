from times import compute_overlap_time, time_range
import pytest

def test_given_input():

    # Assert 1 - test should pass
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(range1, range2) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

    # Assert 2 - test should work 
    range5 = time_range("2001-01-12 10:00:00", "2010-01-12 12:00:00")
    range6 = time_range("2001-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(range5, range6) 
    expected = [('2001-01-12 10:30:00', '2005-07-13 22:37:00'), ('2005-07-13 22:38:00', '2010-01-12 10:45:00')]
    assert result == expected

     # Assert 2 - test should fail (value error in range time / instead of -)
    range3 = time_range("2010-01-12 10:00:00", "2010-01/12 12:00:00")
    range4 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(range3, range4) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

