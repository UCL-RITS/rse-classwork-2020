from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    before = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    after = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    expected = []
    assert compute_overlap_time(before, after) == expected

def test_multiple_overlaps():
    three_hours_with_two_fifteen_minute_breaks = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900)
    two_ranges_splitting_the_first_break = time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2, 120)
    expected = [("2010-01-12 10:40:00","2010-01-12 10:50:00"), ("2010-01-12 11:05:00", "2010-01-12 11:20:00")]
    assert compute_overlap_time(three_hours_with_two_fifteen_minute_breaks, two_ranges_splitting_the_first_break) == expected

def test_touching_edges():
    before = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    after = time_range("2010-01-12 11:00:00", "2010-01-12 12:45:00")
    expected = []
    assert compute_overlap_time(before, after) == expected
