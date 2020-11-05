from times import compute_overlap_time, time_range
import pytest


@pytest.mark.parametrize('time_range1, time_range2, expected', [
        (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), 
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),

        (time_range("2009-01-12 10:00:00", "2009-01-12 12:00:00"), 
        time_range("2001-01-12 10:30:00", "2001-01-12 10:45:00", 2, 60),
        [])

        ])

def test_eval(time_range1, time_range2, expected):
    # Assert 1 - test should pass
    result = compute_overlap_time(time_range1, time_range2) 
    assert result == expected

def test_backwards():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")


