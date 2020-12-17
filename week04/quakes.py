"""A script to find the biggest earthquake in an online dataset."""

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.

## At the top of the file, import any libraries you will use.
import requests
import json

## get the data from the web result
quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

## parse the data as JSON
requests_json = json.loads(quakes.text)

## investigate data to see its structure
# see type of data
print(type(requests_json))  # dict

# see keys within dictionaries
print(requests_json.keys())
    # dict_keys(['type', 'metadata', 'features', 'bbox'])

# see amount of entries in a list
print(len(requests_json['features']))  # 120
print(requests_json['features'][0].keys())
    # dict_keys(['type', 'properties', 'geometry', 'id'])
print(requests_json['features'][0]['properties'].keys())
    # dict_keys(['mag', 'place', 'time', 'updated', 'tz', 'url', 'detail', 'felt', 'cdi', 'mmi', 'alert', 'status', 'tsunami', 'sig', 'net', 'code', 'ids', 'sources', 'types', 'nst', 'dmin', 'rms', 'gap', 'magType', 'type', 'title'])
print(requests_json['features'][0]['properties']['mag'])    #2.6
print(requests_json['features'][0]['geometry'])
    # {'type': 'Point', 'coordinates': [-2.81, 54.77, 14]}

# EXTRA: check the metadata
print(len(requests_json['metadata']))   #6
print(requests_json['metadata'].keys()) 
    # dict_keys(['generated', 'url', 'title', 'status', 'api', 'count'])


# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

## Find the largest quake magnitude
earthquakes = requests_json['features']

max_so_far = earthquakes[0]
for quake in earthquakes:
    if quake['properties']['mag'] > max_so_far['properties']['mag']:
        max_so_far = quake

max_magnitude = max_so_far['properties']['mag']

## Find the location of the largest quake
coords = max_so_far['geometry']['coordinates']

## Print the results
print(f'\nThe maximum magnitude is {max_magnitude}.')
print(f'It occured at coordinates {coords}.')
        # The maximum magnitude is 4.8
        # It occured at coordinates [-2.15, 52.52, 9.4].
