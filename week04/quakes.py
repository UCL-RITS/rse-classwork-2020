"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json
import numpy as np

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

def json_file_load(response):
    """ loads response body into json format """
    dataJson = json.loads(response.text)
    return dataJson

def get_earthquake_magnitude_location(quakeJson):
    """ retrieves magnitude, coordinates and location of earthquakes from the json data """
    magnitudeAndLocation = np.array([[ft['properties']['mag'], ft['geometry']['coordinates'], ft['properties']['place']] for ft in quakeJson['features']], dtype=object)
    return magnitudeAndLocation

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...

    #get data from URL
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

    magnitudeData = get_earthquake_magnitude_location(json_file_load(quakes))

    maxmag, coords, place = [np.max(magnitudeData, axis=0)[0], np.max(magnitudeData, axis=0)[1], np.max(magnitudeData, axis=0)[2]]

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    #print(f"The maximum magnitude is {maxmag} "
        #  f"and it occured at coordinates {coords}, "
        #  f"in {place}.")

    print('the max mag was at', maxmag, 'at coords', coords, 'in', place)
