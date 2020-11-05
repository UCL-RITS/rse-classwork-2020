from times import compute_overlap_time, time_range
import pytest


@pytest.mark.parametrize("time_1, time_2, expected",
[(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
[("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]),
(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
time_range("2008-01-12 10:00:00","2009-01-12 10:00:00"),
[]),
(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
time_range("2010-01-12 12:00:00", "2010-01-13 12:00:00"),
[("2010-01-12 12:00:00","2010-01-12 12:00:00" )]),
(time_range("2010-01-12 10:00:00", "2010-01-12 12:01:00",2, 60),
time_range("2010-01-12 10:30:00", "2010-01-12 11:15:00", 2, 60),
[("2010-01-12 10:30:00","2010-01-12 10:52:00"), ("2010-01-12 10:53:00","2010-01-12 11:00:00"),
("2010-01-12 11:01:00","2010-01-12 11:15:00")])
])
def test_time_overlap(time_1, time_2, expected):


    assert compute_overlap_time(time_1, time_2) == expected

"""
def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    time_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    time_2 = time_range("2008-01-12 10:00:00","2009-01-12 10:00:00" )
    expected = []
    assert compute_overlap_time(time_1,time_2) == expected

def test_touching_boundary():
    touching_time_1  = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    touching_time_2 = time_range("2010-01-12 12:00:00", "2010-01-13 12:00:00")
    expected = []
    assert compute_overlap_time(touching_time_1, touching_time_2) == expected

def test_multiple_overlaps():
    overlap_time_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:01:00",2, 60)
    overlap_time_2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:15:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:52:00"), ("2010-01-12 10:53:00","2010-01-12 11:00:00"),
    ("2010-01-12 11:01:00","2010-01-12 11:15:00")]

    assert compute_overlap_time(overlap_time_1,overlap_time_2) == expected

"""
def test_negative_time():

    with pytest.raises(ValueError):
        time_range("2010-01-12 10:00:00", "2009-01-12 12:00:00")

        
        #assert e.match("Start time must come before end time")

overlap_time_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:01:00",2, 60)
overlap_time_2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:15:00", 2, 60)


print(overlap_time_1)
print(overlap_time_2)
print(compute_overlap_time(overlap_time_1,overlap_time_2))

