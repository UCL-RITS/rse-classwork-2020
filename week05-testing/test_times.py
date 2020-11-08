from times import compute_overlap_time,time_range
from pytest import raises
# import times as ts
import datetime

#Answers UCL-RITS/rse-classwork-2020#

test_data = [ 
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
    time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
    [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
    (time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"),
    time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
    []),
    (time_range("2010-01-12 10:00:00", "2010-01-12 14:00:00", 3, 1800),
    time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
    [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
    time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
    [])
]


@pytest.mark.parametrize("time_range_1,time_range_2,expected",test_data)

def test_overlap_time(range1,range2,expected):
    result = compute_overlap_time(range1,range2)
    assert result == expected


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
