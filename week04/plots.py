"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json
import datetime
import numpy as np
from matplotlib import pyplot as plt


# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2020-12-31",
                          "orderby": "time-asc"}
                      )
    # parsing the data as JSON
    quakes_json = json.loads(quakes.text)
    # obtaining a list of earthquake magnitudes
    time_list = [quakes_json['features'][i]['properties']['time'] for i in range(quakes_json['metadata']['count'])] 
    # converting time from Unix to "normal"
    time_list_year = [datetime.date.fromtimestamp(time_list[i]/1000).year for i in range(quakes_json['metadata']['count'])]
    # counting the occurance of each year
    time_list_year_unique = np.unique(time_list_year,return_counts=True)
    
    # Plotting Frequency vs Year
    plt.figure()
    plt.bar(time_list_year_unique[0],time_list_year_unique[1])
    plt.title("Number of Earthquakes in the UK per year between 2000-2020")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.savefig("EarthquakeFreq00to20.png")
