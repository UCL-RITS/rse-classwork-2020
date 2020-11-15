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
    

#def test_given_input():

 #   large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
 #   short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
 #   
 #   result = compute_overlap_time(large, short)
 #   expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
 #   assert result == expected

#def test_no_overlap():

#    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#    short = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00")
#    
#    result = compute_overlap_time(large, short)
#    expected = []
#    assert result == expected

#def test_later_start_time():
#    with raises(ValueError) as exception:
#        time_range("2010-01-12 10:00:00", "2010-01-10 12:00:00")


#large1=time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#small1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#expected1 = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

#large2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#small2 = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00")
#expected2 = []


