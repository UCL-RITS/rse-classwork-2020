"""The file to test times.py"""

#import functions from times.py
import pytest
from times import compute_overlap_time, time_range

# test for a generic case
def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    # (For now, you copy the output of the times.py program as the expected value
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    
    assert  result == expected

#test for no overlap
def test_no_overlap():
    before = time_range("2010-01-12 10:00:0", "2010-01-12 11:00:00")
    after = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)

    expected = []   #no overlap
    result = compute_overlap_time(before, after)
    assert result == expected

#test for multiple intervals that overlap
def test_multiple_overlaps():
    three_hours_with_two_fifteen_minute_breaks = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900)
        # gives three intervals with two 15min breaks in between
    two_ranges_splitting_the_first_break = time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2, 120)
        # gives two intervals with a 2 min break in between
    
    expected = [("2010-01-12 10:40:00","2010-01-12 10:50:00"), ("2010-01-12 11:05:00", "2010-01-12 11:20:00")]
    result = compute_overlap_time(three_hours_with_two_fifteen_minute_breaks, two_ranges_splitting_the_first_break)
    assert result == expected

#test for touching edges, but no overlap
def test_touching_edges():
    before = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    after = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")

    expected = [] #no overlap
    result = compute_overlap_time(before, after)
    assert result == expected

#negative test for a date going backwards
# first possible solution
def test_negative_time_range():
    with pytest.raises(ValueError) as e:
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
    # lines after the error is raised are not executed in the pytest.raises context, so the assertion has to be outside the "with"    
    assert e.match('The end of the time range has to come strictly after its start.')

# an alternative solution for using pytest.raises to check that the error message is as expected  
def test_negative_time_range_alternative():
    expected_error_message = 'The end of the time range has to come strictly after its start.'
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")