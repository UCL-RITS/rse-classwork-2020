# import ...

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
from datetime import datetime
import json
import requests
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from collections import defaultdict
from statistics import mean 
def get_quake_data_from_URL():
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
    #print(quakes.text[0:100])

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    #print(f"The maximum magnitude is {max_magnitude} "
    #      f"and it occured at coordinates {coords}.")

    with open('quakes.json', 'w') as quakes_js:
        quakes_js.write(quakes.text)

    with open('quakes.json', 'r') as target:
        myfile_str = target.read()

    myfile = json.loads(myfile_str)

    return myfile

def get_max_mag_quake_detail(json_file):

    quake_detail =[]
    features = [dict(feature) for feature in myfile['features']]

    for i in range(len(features)):
        if 'United Kingdom' in features[i]['properties']['place']:
            x = features[i]['properties']['time']
            d = datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d')
            quake_detail.append([features[i]['properties']['mag'],d,features[i]['properties']['place'],features[i]['geometry']['coordinates'] ])
    
    return quake_detail

def draw_freq(magnitude, dates):

    bins = np.arange(min(dates), max(dates)+1)
    plt.figure(figsize = (10,5))    
    plt.title('Frequency of Quakes per Year')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.yticks(range(21))
    plt.grid(linestyle='dotted', linewidth=1) 
    plt.hist(dates, bins-0.5, rwidth = 0.75)
    
    return plt.savefig('Frequency.png')

def draw_mean_mag_bar(magnitude, dates):

    d = defaultdict(list)
    for key, value in zip(dates, magnitude):
        d[key].append(value)

    years = [key for key in dict(d)]
    mean_mag = [round(mean(values),2) for key, values in dict(d).items()]

    plt.figure(figsize = (10,10))    
    plt.bar(years, height = mean_mag)
    plt.xticks(years)
    plt.yticks(mean_mag)
    plt.xlabel('Year')
    plt.ylabel('Mean Magnitude')
    plt.title('Average Magnitude of Quakes by Year')
    plt.ylim(min(mean_mag)-0.05)
    plt.grid(linestyle='dotted', linewidth=1)

    return plt.savefig('Mean_magnitude_bar.png')


def draw_mean_mag_line(magnitude, dates):

    d = defaultdict(list)
    for key, value in zip(dates, magnitude):
        d[key].append(value)

    years = [key for key in dict(d)]
    mean_mag = [round(mean(values),2) for key, values in dict(d).items()]

    plt.figure(figsize = (10,5))   
    plt.xticks(years)
    plt.yticks(mean_mag)
    plt.xlabel('Year')
    plt.ylabel('Mean Magnitude')
    plt.title('Average Magnitude of Quakes by Year')  
    plt.grid(linestyle='dotted', linewidth=1) 
    plt.plot(years, mean_mag)

    return plt.savefig('Mean_magnitude_line.png')

if __name__ == "__main__":
    # ...do things here to find the results...
    myfile = get_quake_data_from_URL()
    details_of_quakes = get_max_mag_quake_detail(myfile)

    magnitude = [details_of_quakes[i][0] for i in range(len(details_of_quakes))]
    dates = [int(details_of_quakes[i][1][0:4]) for i in range(len(details_of_quakes))]

    draw_mean_mag_bar(magnitude, dates)
    draw_freq(magnitude, dates)
    draw_mean_mag_line(magnitude, dates)
