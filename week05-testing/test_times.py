from times import time_range, compute_overlap_time
import datetime
import pytest
from pytest import raises

@pytest.mark.parametrize("time_range_1, time_range_2, expected", [
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
    time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
    [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]), 

    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
    time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00"),
    0), 

    (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60),
    time_range("2010-01-12 10:50:00", "2010-01-12 11:01:00", 2, 120),
    [('2010-01-12 10:50:00', '2010-01-12 10:54:30'), ('2010-01-12 10:56:30', '2010-01-12 11:00:00')]),
    
    (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
    time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"),
    [('2010-01-12 11:00:00', '2010-01-12 11:00:00')])

])
    


def test_eval(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2) 
    assert result == expected

def test_negative_time():       
    with raises(TypeError) as exception:
        range1 = time_range("2010-01-12 13:00:00", "2010-01-12 11:00:00")