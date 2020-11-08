from times import compute_overlap_time, iss_passes, time_range
import yaml
import pytest
from pytest import raises
# needed to add to example to get to work.
import mock
import datetime

#testing file
with open("fixture.yml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)

@pytest.mark.parametrize("test_name", fixture)
# fixture is a list of dictionaries [{'generic':...}, {'no_overlap':...}, ...]

def test_eval(test_name):
 # test_name will be a dictionary, e.g. for the first case: {'generic': {'time_range_1':..., 'time_range2':..., 'expected':...}
    properties = list(test_name.values())[0]
    first_range = time_range(*properties['time_range_1'])
    second_range = time_range(*properties['time_range_2'])
    expected = [(start, stop) for start, stop in properties['expected']]
    assert compute_overlap_time(first_range, second_range) == expected

def test_time_back():

    start_time = "2010-01-12 12:00:00"
    end_time = "2010-01-12 10:00:00"

    with raises(ValueError):
        time_range(start_time, end_time)

class ISS_response:
    '''
    This class provides "hardcoded" return values to mock the calls to the online API.
    '''
    @property
    def status_code(self):
        return 200

    def json(self):
    #    '''
    #   mocks the bit from the json output we need from querying the API.
    #    '''
        now = datetime.datetime.now().timestamp()
        return {'message': 'success',
                'request': {'altitude': 10.0, 'datetime': now, 'latitude': 51.5074, 'longitude': -0.1278, 'passes': 5},
                'response': [{'duration': 446, 'risetime': now + 88433},
                             {'duration': 628, 'risetime': now + 94095},
                             {'duration': 656, 'risetime': now + 99871},
                             {'duration': 655, 'risetime': now + 105676},
                             {'duration': 632, 'risetime': now + 111480}]}

def test_iss_passes():
    with mock.patch("requests.get", new=mock.MagicMock(return_value=ISS_response())) as mymock:
        iss_over_London = iss_passes(51.5074, -0.1278)
        mymock.assert_called_with("http://api.open-notify.org/iss-pass.json",
                                  params={
                                      "lat": 51.5074,
                                      "alt":10, # needed to add to example to get to work.
                                      "lon": -0.1278,
                                      "n": 5})
        assert len(iss_over_London) == 5
        # Create a range from yesterday to next week whether the overlap ranges are still 5
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        next_week = datetime.datetime.now() + datetime.timedelta(days=7)
        large = time_range(f"{yesterday:%Y-%m-%d %H:%M:%S}", f"{next_week:%Y-%m-%d %H:%M:%S}")
        assert compute_overlap_time(large, iss_over_London) == iss_over_London
