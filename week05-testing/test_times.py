from times import compute_overlap_time, time_range
import pytest
import yaml

with open('week05-testing/fixture.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader) # or safe_load(f)
    print(data) # gives a list of nested dictionary 

@pytest.mark.parametrize('test', data) 
def test_eval(test):
    list_test = list(test.values())
    range1 = time_range(*(list_test[0]['time_range1'])) # tuple
    range2 = time_range(*(list_test[0]['time_range2']))
    expected = [(interval1, interval2) for interval1, interval2 in list_test[0]['expected']] # for loop needed for 2 or more intervals 
    result = compute_overlap_time(range1, range2)
    assert result == expected

def test_backwards():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

