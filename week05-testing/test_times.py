import times
import pytest

class TestTimeOverlap:
    """TestTimeOverlap class contains all functions involved in
    testing the overlap of two times based on example UCL RITS code"""

    def test_given_input(self):
        """Tests hardcoded input given as part of the example problem"""
        result = times.compute_overlap_time(times.large, times.short)
        expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        assert result == expected

    def test_non_overlapping_times(self):
        """Tests two time ranges that do not overlap"""
        t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        t2 = times.time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
        result = times.compute_overlap_time(t1, t2)
        expected = []
        assert result == expected

    def test_several_intervals(self):
        """Tests intervals where two intervals overlap"""
        t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 0)
        t2 = times.time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2, 0)
        result = times.compute_overlap_time(t1, t2)
        expected = [('2010-01-12 10:30:00', '2010-01-12 11:00:00'),('2010-01-12 11:00:00', '2010-01-12 11:30:00')]
        assert result == expected

    def test_touching_times(self):
        """Tests intervals where one finishes at the same time another starts"""
        t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        t2 = times.time_range("2010-01-12 12:00:00", "2010-01-12 12:30:00")
        result = times.compute_overlap_time(t1, t2)
        expected = []
        assert result == expected

    def test_negative_time_interval(self):
        """Tests a time range which goes backwards"""
        t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        t2 = times.time_range("2010-01-12 11:00:00", "2010-01-12 10:30:00")
        with pytest.raises(ValueError):
            times.compute_overlap_time(t1, t2)
