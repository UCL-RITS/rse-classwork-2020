from times import compute_overlap_time,time_range
from pytest import raises
import pytest
import yaml
# import times as ts
import datetime

# Answers UCL-RITS/rse-classwork-2020#

with open("fixture.yaml", 'r') as yamlfile:
    fixture = yaml.load(yamlfile, Loader=yaml.FullLoader)

# https://docs.pytest.org/en/stable/example/parametrize.html

@pytest.mark.parametrize("test_name", fixture)  
def test_overlap_time(test_name):
    information = list(test_name.values())[0]
    
    # use '*' since we do not know the value of 'number of intervals' within 'time_range' function
    range_1 = time_range(*information['time_range_1'])
    range_2 = time_range(*information['time_range_2'])
    expected = [(start, stop) for start, stop in information['expected']]
    
    assert compute_overlap_time(range_1, range_2) == expected

# def test_given_input(): 
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

#     result = compute_overlap_time(range1,range2)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] #expected output
#     assert result == expected

# def two_no_overlap(): # two time ranges that do not overlap
#     range1 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
#     range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

#     result = compute_overlap_time(range1,range2)
#     expected = [] #expected output
#     assert result == expected

# def two_several_interval(): # two time ranges that both contain several intervals each
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 14:00:00", 3, 1800)
#     # range1_expected = ('2010-01-12 10:00:00','2010-01-12 11:00:00'),('2010-01-12 11:30:00','2010-01-12 12:30:00'),('2010-01-12 13:00:00','2010-01-12 14:00:00')
#     range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

#     result = compute_overlap_time(range1,range2)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] #expected output
#     assert result == expected

# def two_same_start_end(): # start time = end time
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")

#     range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

#     result = compute_overlap_time(range1,range2)
#     expected = [] #expected output
#     assert result == expected

# def backwards_negative_test(): # Negative tests - Test that something that is expected to fail actually does fail
#     range1 = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
#     range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

#     with raises(ValueError):
#         compute_overlap_time(range1,range2)
        
# Testing area

#test_given_input()
#two_no_overlap()
#two_several_interval()
#two_same_start_end()
#backwards_negative_test()
