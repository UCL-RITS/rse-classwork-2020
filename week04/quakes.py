"""A script to find the biggest earthquake in an online dataset."""

import requests
import json
import numpy as np 


if __name__ == "__main__":
    #reads in data from the internet url given 
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                     params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"})
    #reads in data using json as a dictionary
    earthquakes = json.loads(quakes.text)

    # creates a list of all the magnitudes of the earthquakes 
    eq_size = [earthquakes['features'][i]['properties']['mag'] for i in range(earthquakes['metadata']['count'])]


    # searches for the location of the largest earthquake within list eq_size
    # location is stored as a list
    location = [j for j in range(len(eq_size)) if eq_size[j] == np.max(eq_size)]

    # gives location of the largest earthqukes
    geog_location = earthquakes['features'][location[0]]['properties']['place']
    
    print(f"The maximum magnitude is {np.max(eq_size)} "
          f"and it occured at  {geog_location}.")
