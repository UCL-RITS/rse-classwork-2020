import times
import pytest
import yaml

with open("./week05-testing/fixtures.yaml", "r") as file:
    fixtures = yaml.safe_load(file)

# Tests that various inputs work as expected for the compute_overlap_time function 
@pytest.mark.parametrize("test_name", fixtures)
def test_given_input(test_name):
    properties = list(test_name.values())[0]
    first_range = times.time_range(*properties['time_range_1'])
    second_range = times.time_range(*properties['time_range_2'])
    expected_overlap = [(start, stop) for start, stop in properties['expected']]
    assert times.compute_overlap_time(first_range, second_range) == expected_overlap

# Testing the right error is raised when inputting time ranges in the wrong order
def test_negative():
    with pytest.raises(ValueError):
        times.time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
