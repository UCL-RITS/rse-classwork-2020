from times import compute_overlap_time, time_range

def test_given_input():

    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(range1, range2) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

