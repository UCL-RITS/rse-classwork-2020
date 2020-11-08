from times import compute_overlap_time
from times import time_range
from pytest import raises
# import times as ts
import datetime

def test_given_input(): 
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(range1,range2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] #expected output
    assert result == expected

def two_no_overlap(): # two time ranges that do not overlap
    range1 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(range1,range2)
    expected = [] #expected output
    assert result == expected

def two_several_interval(): # two time ranges that both contain several intervals each
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 14:00:00", 3, 1800)
    # range1_expected = ('2010-01-12 10:00:00','2010-01-12 11:00:00'),('2010-01-12 11:30:00','2010-01-12 12:30:00'),('2010-01-12 13:00:00','2010-01-12 14:00:00')
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(range1,range2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] #expected output
    assert result == expected

def two_same_start_end(): # start time = end time
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")

    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    result = compute_overlap_time(range1,range2)
    expected = [] #expected output
    assert result == expected

def backwards_negative_test(): # Negative tests - Test that something that is expected to fail actually does fail
    range1 = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    with raises(ValueError):
        compute_overlap_time(range1,range2)
        
   
# Testing area

#test_given_input()
#two_no_overlap()
#two_several_interval()
#two_same_start_end()
backwards_negative_test()
