import times

def test_given_input():

    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
  
    assert result == expected

