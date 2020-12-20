"""The file to test times.py"""

#import functions from times.py
import pytest
import yaml
from times import compute_overlap_time, time_range

# get fixture data from yaml file  
with open("fixture.yaml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)
    print(fixture)
        # gives a list of dictionaries for each test case

# parametrization of entries
@pytest.mark.parametrize("test_name", fixture)
# fixture is a list of dictionaries [{'generic':...}, {'no_overlap':...}, ...]

def test_parametrized_overlap(test_name):
    # test_name will be a dictionary, e.g. for the first case: {'generic': {'time_range_1':..., 'time_range2':..., 'expected':...}}
    properties = list(test_name.values())[0]
    first_range = time_range(*properties['time_range_1'])
    second_range = time_range(*properties['time_range_2'])
   
    expected = [(start, stop) for start, stop in properties['expected']]
    result = compute_overlap_time(first_range, second_range)
    assert result == expected

#negative test for a date going backwards
#check that the error message matches with the one raised in time_range function of times.py

# first possible solution
def test_negative_time_range():
    with pytest.raises(ValueError) as e:
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
    # lines after the error is raised are not executed in the pytest.raises context, so the assertion has to be outside the "with"    
    assert e.match('The end of the time range has to come strictly after its start.')

# an alternative solution for using pytest.raises to check that the error message is as expected  
def test_negative_time_range_alternative():
    expected_error_message = 'The end of the time range has to come strictly after its start.'
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")