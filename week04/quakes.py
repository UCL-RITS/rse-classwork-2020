"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import json 
import requests
from matplotlib import pyplot as plt
import datetime

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

def url_text(url, params):
    quakes = requests.get(url, params)
    # print(quakes.text)
    quakes_json = json.loads(quakes.text)
    # print(json.dumps(quakes_json, indent=4))

    return quakes_json


def find_earthquake():
    quakes_json = url_text("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                {'starttime': "2000-01-01",
                    "maxlatitude": "58.723",
                    "minlatitude": "50.008",
                    "maxlongitude": "1.67",
                    "minlongitude": "-9.756",
                    "minmagnitude": "1",
                    "endtime": "2020-10-11",
                    "orderby": "time-asc" })


    quakes_mag_list = []
    for feature in quakes_json['features']:
        magnitude = feature['properties']['mag']
        quakes_mag_list.append(magnitude)

    max_magnitude = max(quakes_mag_list)

    coords_list = []

    # 2 found to be max magnitude so 2 different places 
    for feature in quakes_json['features']:
        if feature['properties']['mag'] == max_magnitude:
            coord = feature['geometry']['coordinates']
            coords_list.append(coord)

    # index = quakes_mag_list.index(max_magnitude)
    # coords = quakes_json['features'][index]['geometry']['coordinates']

    # print(coords)
    return max_magnitude, coords_list


def plot():
    quakes_json = url_text("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                    {'starttime': "2000-01-01",
                        "maxlatitude": "58.723",
                        "minlatitude": "50.008",
                        "maxlongitude": "1.67",
                        "minlongitude": "-9.756",
                        "minmagnitude": "1",
                        "endtime": "2020-10-11",
                        "orderby": "time-asc" })
    
    dict = {}
    for earthquake in quakes_json['features']:
        year = datetime.datetime.fromtimestamp(earthquake['properties']['time']/1000).year
        # print(year)
    
        if year in dict.keys():
            dict[year] = dict[year] + 1
        else:
            dict[year] = 1

    number_quakes = dict.values()
    years = dict.keys()

    plt.plot(years, number_quakes)
    plt.title('frequency (number) of earthquakes per year')
    plt.show() 

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
      
    [max_magnitude, coords] = find_earthquake()
    plot()

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.

    print(f'The maximum magnitude is {max_magnitude} '
          f'and it occured at coordinates {coords}.')

    

