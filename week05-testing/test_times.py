import datetime
import pytest
import yaml
import mock
from times import compute_overlap_time, time_range, iss_passes

with open("fixture.yaml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)
    print(fixture)
    
@pytest.mark.parametrize("test_name", fixture)
# fixture is a list of dictionaries [{'generic':...}, {'no_overlap':...}, ...]

def test_time_range_overlap(test_name):
    # test_name will be a dictionary, e.g. for the first case: {'generic': {'time_range_1':..., 'time_range2':..., 'expected':...}
    properties = list(test_name.values())[0]
    first_range = time_range(*properties['time_range_1'])
    second_range = time_range(*properties['time_range_2'])
    expected_overlap = [(start, stop) for start, stop in properties['expected']]
    assert compute_overlap_time(first_range, second_range) == expected_overlap

def test_negative_time_range():
    with pytest.raises(ValueError) as e:
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
        assert e.match('The end of the time range has to come strictly after its start.')

class ISS_response:
    '''
    This class provides "hardcoded" return values to mock the calls to the online API.
    '''
    @property
    def status_code(self):
        return 200

    def json(self):
        '''
        mocks the bit from the json output we need from querying the API.
        '''
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
                                      "lon": -0.1278,
                                      "n": 5})
        assert len(iss_over_London) == 5
        # Create a range from yesterday to next week whether the overlap ranges are still 5
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        next_week = datetime.datetime.now() + datetime.timedelta(days=7)
        large = time_range(f"{yesterday:%Y-%m-%d %H:%M:%S}", f"{next_week:%Y-%m-%d %H:%M:%S}")
        assert compute_overlap_time(large, iss_over_London) == iss_over_London
        
# def test_given_input():
    
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
#     result = compute_overlap_time(large, short) 
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_negative():
#     with pytest.raises(valueerror):
#         time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

