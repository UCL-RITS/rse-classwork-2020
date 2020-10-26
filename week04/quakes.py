"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json
from datetime import datetime
import numpy as np

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):

def load_as_json(response):
    '''Loads reponse body into json format for easier information extraction'''
    jsondata = json.loads(response.text)
    return jsondata

def get_quake_time(response, quakeno):
    '''Prints quake time using quake number from response data'''
    # Response data is automatically given as a UNIX timestamp (ms)
    print(datetime.fromtimestamp(json.loads(response.text)['features'][quakeno]['properties']['time']/1000))

def get_quake_mag_loc(datajson):
    '''Stores magnitudes and locations of all earthquakes in a list from json data'''
    magloc = np.array([ [f['properties']['mag'], f['geometry']['coordinates'], f['properties']['place']] for f in datajson['features']], dtype=object)
    # Returns n  x  3  array for n entries
    return magloc

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...

    # Pull data from URL
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

    maglocdata = get_quake_mag_loc(load_as_json(quakes))

    # Get maximum from array data
    max_magnitude, coords = [np.max(maglocdata, axis=0)[0], np.max(maglocdata, axis=0)[1]]
    
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
