"""A script to find the biggest earthquake in an online dataset."""
import requests
import json
import numpy as np
import pandas as pd
import inflect
import matplotlib.pyplot as plt
from datetime import datetime
import time
# At the top of the file, import any libraries you will use.
# import ...

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...
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
data = json.loads(quakes.text)

quakesdata = pd.json_normalize(data['features'])

with open('quakes.json', 'w') as json_file:
    json_file.write(quakes.text)
# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
    max_magnitude=0;
    coords=[];
    for quake in data['features']:
        if quake['properties']['mag'] > max_magnitude:
            max_magnitude=quake['properties']['mag']
            coords.clear()
            coords.append(quake['geometry']['coordinates'])

        if quake['properties']['mag'] == max_magnitude:
            coords.append(quake['geometry']['coordinates'])


    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")

    quakesdata['properties.time'] = quakesdata['properties.time'].apply(
        lambda x: datetime.fromtimestamp(x / 1000))
    #print(quakesdata['properties.time'])

    yearly_quakes = quakesdata['properties.mag'].groupby(quakesdata['properties.time'].dt.year).agg(
        ['mean', 'count'])
    years = yearly_quakes.index.tolist();

    xtick = np.arange(np.min(years), np.max(years)+1)

    plt.figure(1)
    plt.plot(years, yearly_quakes['count'])
    plt.xlabel('year')
    plt.ylabel('count')
    plt.title('yearly quake number')
    plt.xticks(xtick,rotation='vertical')
    plt.savefig('quake_number_each_year.png')
    plt.show()

    plt.figure(2)
    plt.plot(years, yearly_quakes['mean'])
    plt.xlabel('year')
    plt.ylabel('mean magnitude')
    plt.title('yearly mean magnitude')
    plt.xticks(xtick, rotation='vertical')
    plt.savefig('mean_magnityude_each_year.png')
    plt.show()

