import times
import pytest

class TestTimeOverlap:
    """TestTimeOverlap class contains all functions involved in
    testing the overlap of two times based on example UCL RITS code"""

    @pytest.mark.parametrize("time_range_1, time_range_2, expected", [
        # Test hardcoded input from example problem
        (times.large, times.short, [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
        # Tests two time ranges that do not overlap
        (times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), times.time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00"), []),
        # Tests intervals where each has several intervals and two sub-intervals overlap
        (times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 0), times.time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2, 0), [('2010-01-12 10:30:00', '2010-01-12 11:00:00'),('2010-01-12 11:00:00', '2010-01-12 11:30:00')]),
        # Tests two intervals where one finishes at exactly the same time another started
        (times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), times.time_range("2010-01-12 12:00:00", "2010-01-12 12:30:00"), [])
                              ])
    def test_given_input(self, time_range_1, time_range_2, expected):
        """Tests hardcoded input given as part of the example problem"""
        result = times.compute_overlap_time(time_range_1, time_range_2)
        assert result == expected

    def test_negative_time_interval(self):
        """Tests a time range which goes backwards"""
        t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        t2 = times.time_range("2010-01-12 11:00:00", "2010-01-12 10:30:00")
        with pytest.raises(ValueError):
            times.compute_overlap_time(t1, t2)
