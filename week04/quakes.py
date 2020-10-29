"""A script to find the biggest earthquake in an online dataset."""

import requests
import json
import datetime
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


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

    #"time": 1579759019614,


    years = set([ datetime.date.fromtimestamp(x["properties"]["time"] / 1e3).year for x in requests_json["features"]])

    frequency_per_year = { year : len([earthquake for earthquake in requests_json["features"] if datetime.date.fromtimestamp(earthquake["properties"]["time"] / 1e3).year == year]) for year in years }
    
    data = list(frequency_per_year.items())
    an_array = np.array(data)
    sorted_array = an_array[np.argsort(an_array[:, 0])]
    #dataset = zip(an_array)


    plt.plot(sorted_array[:,0],sorted_array[:,1])
    plt.xlabel('Years')
    plt.ylabel('Frequency')
    plt.title('Earthquake Frequency in the UK')
    plt.show()
    #print(frequency_per_year)




    #print(requests_json['features'][0])
    #dict_keys = requests_json.keys()

    # max_magnitude = requests_json['features'][0]['properties']['mag']
    # max_data = requests_json['features'][0]
    # for data in  requests_json['features']:

        # if (magnitude>max_magnitude):
        #     #print(magnitude)
        #     max_magnitude = magnitude
        #     max_data = data

    # coords = max_data['geometry']['coordinates'][0:2]
    # #long, lat  = coords
    # print(f"The maximum magnitude is {max_magnitude} "
    #       f"and it occured at coordinates {coords}.")
    
