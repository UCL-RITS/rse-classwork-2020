import requests
import json
import numpy as np 
from datetime import datetime
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # ...do things here to find the results...

    max_magnitude = 0
    coords = {}
    
    # this block of code gets the data of all the earthquakes that occured in UK in the last century (1900-1999)
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
                    
   

    requests_json = json.loads(quakes.text[:])

    # a list that stores the magnitude and the time of every earthquake
    mag_year = [[item['properties']['mag'],item['properties']['time']] for item in requests_json['features']]
    
    #for every year we create a position in the array. Initially is zero.
    # index 0 -- > 2000
    # index 1 -- > 2001 
    #... etc
    list_avg_mag = np.zeros(2018 - 2000 + 1) 
    list_num_quakes = np.zeros(2018 - 2000 + 1)

    for year in range(2000,2019):
        avg_mag = [] # stores the values of magnitude for an earthquake that happened in a specific year
        for item in mag_year:
            if int(datetime.utcfromtimestamp(item[1]/1000.0).strftime('%Y')) == year:
                avg_mag.append(item[0])
        if len(avg_mag) > 0:    # some years (2012,2016) have no values and we need to check that
            list_avg_mag[year-2000] = np.average(avg_mag)
            list_num_quakes[year-2000] = np.sum(avg_mag)
    
    years = [i for i in range(2000,2019)] # the x-axis

    plt.plot(years, list_avg_mag, 'ro') # Scattered diagram
    plt.xticks(np.arange(min(years), max(years)+1, 1.0)) # the interval in the x axis increases by 1
    plt.xlabel("year")
    plt.ylabel("average magnitude")
    plt.show() # plot the figure

    plt.plot(years, list_num_quakes, 'ro')
    plt.xticks(np.arange(min(years), max(years)+1, 1.0)) # the interval in the x axis increases by 1
    plt.xlabel("year")
    plt.ylabel("number of earthquakes")
    plt.show() # plot the figure

    