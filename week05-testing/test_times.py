from times import compute_overlap_time, time_range
import pytest
import requests
import mock 
import yaml

with open('week05-testing/fixture.yaml', 'r') as f:
    data_dictionary = yaml.load(f, Loader=yaml.FullLoader) # or safe_load(f)
    # gives a list of nested dictionary 

@pytest.mark.parametrize('test', data_dictionary)
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

'''
def test_iss_passes():
    with mock.patch.object(requests, 'get') as mock_get:
        iss_london = iss_passes(51.5074, -0.1278)
        mock_get.assert_called_with("http://api.open-notify.org/iss-pass.json",
                                    params={
                                            'lat': 51.5074,
                                            'lon': -0.1278,
                                            'n': 5
                                    })

        # assert len(iss_london) == 5
'''