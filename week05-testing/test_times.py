# Test file for the times.py file

from times import time_range, compute_overlap_time # Importing the necessary functions from times.py
import pytest

# Testing that the output of compute_overlap_time is as expected 
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

# Testing that we obtain an empty list when there is no overlap between our ranges
def test_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-30 13:00:00", "2010-01-30 14:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

# Testing that ranges with the same end in range 1 as start in range 2 returns an empty list
def test_same_start_end():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

# Testing the right error is raised when inputting time ranges in the wrong order
def test_negative():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
