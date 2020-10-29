"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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
                          "orderby": "time-asc"} # easiest way would be just to change this to "magnitude-asc"?
                      )

    quakes_json = json.loads(quakes.text) # convert text body to json format

    with open('quake_data.json', 'w') as file_to_write:
        file_to_write.write(quakes.text)

    max_magnitude = 0
    max_magnitude_index = 0
    for i in range(len(quakes_json['features'])):
        test_magnitude = quakes_json['features'][i]['properties']['mag']
        if test_magnitude > max_magnitude:
            max_magnitude = test_magnitude
            max_magnitude_index = i

    coords = quakes_json['features'][max_magnitude_index]['geometry']['coordinates']

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")


    ### The plotting part of the task
    frequency_dict = {}

    for i in range(len(quakes_json['features'])):
        ts = int(quakes_json['features'][i]['properties']['time'])/1000 # reading UNIX Epoch format datetime, in milliseconds (hence divide by 1000)         
        quake_datetime = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') # saving the year of the earthquake
        quake_year = int(quake_datetime[:4]) # saving just the year
        
        # adding 
        if quake_year in frequency_dict.keys():
            frequency_dict[quake_year] += 1
        else:
            frequency_dict[quake_year] = 1
    
    print(frequency_dict)

    # plotting frequencies
    lists = sorted(frequency_dict.items()) # sorted by key, return a list of tuples
    years, frequencies = zip(*lists) # unpack a list of pairs into two tuples
    plt.figure()
    plt.plot(years, frequencies)
    plt.show()
    plt.savefig("frequencies_plot.pdf")
    
