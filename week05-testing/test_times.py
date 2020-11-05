from times import compute_overlap_time, time_range
import pytest

@pytest.mark.parametrize('time_range1, time_range2, expected',[
    #Test 1
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60), ('2010-01-12 12:30:00', '2010-01-12 12:00:00'), ('2010-01-12 12:38:00', '2010-01-12 12:00:00')),
    #Test 2
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')),
    #Test 3
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,0),time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 0), [('2010-01-12 10:30:00', '2010-01-12 10:37:30'), ('2010-01-12 10:37:30', '2010-01-12 10:45:00'), ('2010-01-12 11:00:00', '2010-01-12 10:37:30'), ('2010-01-12 11:00:00', '2010-01-12 10:45:00')]),
    #Test 4
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60),('2010-01-12 12:00:00', '2010-01-12 12:00:00'), ('2010-01-12 12:23:00', '2010-01-12 12:00:00')),
    #Test 5
    #(time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00"), [], []])
    ])
def test(time_range1, time_range2, expected):
    result = compute_overlap_time(time_range1, time_range2)
    assert result == expected


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 12:30:00', '2010-01-12 12:00:00'), ('2010-01-12 12:38:00', '2010-01-12 12:00:00')]
    assert result == expected

 #def test_no_overlap():
    #Time ranges that do not overlap
    #large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    #short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    #result = compute_overlap_time(large,short)
    #expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    #assert result == expected

def test_sev_int():  
    #Time ranges with several intervals
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,0)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 0)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:30'), ('2010-01-12 10:37:30', '2010-01-12 10:45:00'), ('2010-01-12 11:00:00', '2010-01-12 10:37:30'), ('2010-01-12 11:00:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_touching_times():
    #Time ranges that end exactly at the same time when the other starts
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00'), ('2010-01-12 12:23:00', '2010-01-12 12:00:00')]
    assert result == expected

#def negative_test():
    #t = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
    #t2 = time_range("2010-01-12 12:00:00", "2010-01-12 11:00:00")
    #with pytest.raises(ValueError):
        #compute_overlap_time(t)
    #result = compute_overlap_time(large,short)
    #expected = [('2010-01-12 12:30:00', '2010-01-12 12:00:00'), ('2010-01-12 12:38:00', '2010-01-12 12:00:00')]
    #assert result == expected
