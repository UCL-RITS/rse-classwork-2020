from times import time_range, compute_overlap_time
import pytest

@pytest.mark.parametrize("first_range, second_range, expected_overlap",[
    (# large, short
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    ),
    (# test not overlap
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00"),
        []
    ),
    (# test multiple intervals
        time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900),
        time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2, 120),
        [("2010-01-12 10:40:00","2010-01-12 10:50:00"), ("2010-01-12 11:05:00", "2010-01-12 11:20:00")]
    ),
    (# test end start
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00"),
        time_range("2010-01-12 10:45:00", "2010-01-12 11:00:00"),
        []
    )
])

def test_time_range_overlap(first_range, second_range, expected_overlap):
    assert compute_overlap_time(first_range, second_range) == expected_overlap





# def test_given_input():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(large,short) 
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
#                 ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_not_overlap():
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     range2 = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
#     restult = compute_overlap_time(range1,range2)
#     expected = 0
#     #assert result == expected #FIXME

# def test_multiple_intervals():
#     range1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 120)
#     expected = [('2010-01-12 10:50:00', '2010-01-12 10:54:30'), ('2010-01-12 10:56:30', '2010-01-12 11:00:00')]
#     result = compute_overlap_time(range1, range2)
#     # assert result == expected # FIXME

# def test_end_start():
#     range1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
#     range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 120)

# def test_input_error():
#     with pytest.raises(ValueError):
#         range1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:15:00")

  

# def test_input_error2():
#     with pytest.raises(ValueError):
#         range1 = time_range("2010-01-12 10:30:00", "2010-01-11 10:30:00")

