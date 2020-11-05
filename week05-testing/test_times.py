from times import time_range, compute_overlap_time
import pytest
import yaml

with open('fixture.yaml', 'r') as file:
    fixture_dict = yaml.load(file, Loader=yaml.FullLoader)

@pytest.mark.parametrize("time_range_1, time_range_2, expected", list(fixture_dict.values()), ids=fixture_dict.keys())
def test_given_input(time_range_1, time_range_2, expected):

    result = compute_overlap_time(time_range_1, time_range_2)

    assert result == expected

def test_backward_date():

    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
