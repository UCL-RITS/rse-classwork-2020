import times

def test_given_input():

    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
  
    assert result == expected

def test_no_overlap_helper():
    assert(
        times.compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
            ('2010-01-12 10:38:00', '2010-01-12 12:20:00')
        ) 
        == tuple()
    )

def test_inside_edge_overlap_helper():
    assert(
        times.compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:30:00', '2010-01-12 10:35:00')
        )
        == ('2010-01-12 10:30:00', '2010-01-12 10:35:00')
    )


def test_same_overlap_helper():
    assert(
        times.compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00')
        )
        == ('2010-01-12 10:30:00', '2010-01-12 10:37:00')
    )

def test_outside_edge_overlap_helper():
    assert(
        times.compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:37:00', '2010-01-12 10:39:00')
        )
        == tuple()
    )

def test_partial_overlap_helper():
    assert(
        times.compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:34:00', '2010-01-12 10:42:00')
        )
        == ('2010-01-12 10:34:00', '2010-01-12 10:37:00')
    )

def test_subset_overlap_helper():
    assert(
        times.compute_overlap_helper(
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
        )
        == ('2010-01-12 10:32:00', '2010-01-12 10:36:30')
    )

