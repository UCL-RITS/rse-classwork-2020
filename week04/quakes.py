"""A script to find the biggest earthquake in an online dataset."""

import requests
import json

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
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

    requests_json = json.loads(quakes.text)

    #dict_keys = requests_json.keys()

    max_magnitude = requests_json['features'][0]['properties']['mag']
    max_data = requests_json['features'][0]
    for data in  requests_json['features']:
        magnitude = data['properties']['mag']
        if (magnitude>max_magnitude):
            #print(magnitude)
            max_magnitude = magnitude
            max_data = data

    coords = max_data['geometry']['coordinates'][0:2]
    #long, lat  = coords
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
