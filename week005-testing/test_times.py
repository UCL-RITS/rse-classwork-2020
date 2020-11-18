from times import time_range
from times import compute_overlap_time
from pytest import raises
import pytest
import yaml

with open('fixture.yaml', 'r') as yaml_file:
    fixture = yaml.safe_load(yaml_file)
    print(fixture)

@pytest.mark.parametrize("test_name", fixture) 
def test_general_overlap(test_name):
    properties = list(test_name.values())[0]
    first_range = time_range(*properties['time_range_1'])
    second_range = time_range(*properties['time_range_2'])
    expected_overlap = [(start, stop) for start, stop in properties['expected']]
    print(properties)
    assert compute_overlap_time(first_range, second_range) == expected_overlap
    
