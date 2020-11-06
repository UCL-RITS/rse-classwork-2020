from times import time_range ,compute_overlap_time, compute_overlap_helper
import pytest

testdata = [[('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:38:00', '2010-01-12 12:20:00'),tuple()] #test_no_overlap_helper
     ,(('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:30:00', '2010-01-12 10:35:00'),('2010-01-12 10:30:00', '2010-01-12 10:35:00')) #test_inside_edge_overlap_helper
     ,(('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:30:00', '2010-01-12 10:37:00')) #test_same_overlap_helper
     ,(('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:37:00', '2010-01-12 10:39:00'),tuple()) #test_outside_edge_overlap_helper
     ,(('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:34:00', '2010-01-12 10:42:00'),('2010-01-12 10:34:00', '2010-01-12 10:37:00')) #test_partial_overlap_helper
     ,(('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:32:00', '2010-01-12 10:36:30'),('2010-01-12 10:32:00', '2010-01-12 10:36:30'))#test_subset_overlap_helper
]

@pytest.mark.parametrize(
    "time_range1,time_range2,expected",testdata
)

def test_eval(time_range1,time_range2,expected):
    assert compute_overlap_helper(time_range1,time_range2) == expected

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected
"""
def test_subset_overlap_helper():
    assert(
        compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
        )
        == ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
    )
"""
def test_negative():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
