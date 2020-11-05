import times
from pytest import raises

def test_given_input():

    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = (times.compute_overlap_time(large, short))
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

def test_non_overlap():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 14:30:00", "2010-01-12 14:45:00", 2, 60)
    result = (times.compute_overlap_time(large, short))
    print (result)
    expected = []

    assert result == expected

def test_several_intervals():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60)
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = (times.compute_overlap_time(large, short))
    print (result)
    expected = [('2010-01-12 10:30:30', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

def test_time_back():

    start_time = "2010-01-12 12:00:00"
    end_time = "2010-01-12 10:00:00"

    with raises(ValueError):
        times.time_range(start_time, end_time)
