import times

class TestTimeOverlap:
    """TestTimeOverlap class contains all functions involved in
    testing the overlap of two times based on example UCL RITS code"""

    def test_given_input(self):
        """Tests hardcoded input given as part of the example problem"""
        result = times.compute_overlap_time(times.large, times.short)
        expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        assert result == expected
