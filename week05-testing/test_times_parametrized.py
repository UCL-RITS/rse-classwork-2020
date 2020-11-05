import times
import pytest

# Tests that various inputs work as expected for the compute_overlap_time function 
@pytest.mark.parametrize('time_range_1, time_range_2, expected', [(times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),(times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), times.time_range("2010-01-30 13:00:00", "2010-01-30 14:00:00"), []), (times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), times.time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00"), [])])
def test_given_input(time_range_1, time_range_2, expected):
    result = times.compute_overlap_time(time_range_1,time_range_2)
    assert result == expected

# Testing the right error is raised when inputting time ranges in the wrong order
def test_negative():
    with pytest.raises(ValueError):
        times.time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
