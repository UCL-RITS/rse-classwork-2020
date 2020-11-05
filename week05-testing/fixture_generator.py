from times import time_range
import yaml

test_params = {
    'generic' : (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
    'no overlap' : (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00"), []),
    'exact  overlap' : (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"), [])
}

with open('fixture.yaml', 'w') as file:
    yaml.dump(test_params, file)