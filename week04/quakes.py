"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import requests
import json
import os
import math
import IPython
from IPython.display import Image
import numpy as np
import matplotlib.pyplot as plt

def request_map_at(lat, long, zoom=10, satellite=True):
    base_url = "https://mt0.google.com/vt?"

    x_coord, y_coord = deg2num(lat, long, zoom)

    params = dict(
        x=int(x_coord),
        y=int(y_coord),
        z=zoom
    )
    if satellite:
        params['lyrs'] = 's'

    return requests.get(base_url, params=params)


def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def get_data():
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
    return quakes


def max_magnitude(features):
    max_mag = 0
    coord_max_mag = []
    for feature in features:
        magnitude = feature["properties"]["mag"]
        coordinates = feature["geometry"]["coordinates"]
        if max_mag < magnitude:
            max_mag = magnitude
            if max_mag == magnitude:
                coord_max_mag.append(coordinates)
            else:
                coord_max_mag = coordinates
    return max_mag, coord_max_mag

def avg_mag(features):
    FIRST_YEAR = 1970
    milliseconds_in_year = 3.154e+10
    current_year = 0
    # avg_mag = []
    data = {}
    for feature in features:
        magnitude = feature["properties"]["mag"]
        # avg_mag.append(magnitude)

        # changing time units of feature to years
        time_in_ms = feature["properties"]["time"]
        time_in_years = time_in_ms / milliseconds_in_year
        year = int(FIRST_YEAR + time_in_years)
        feature["properties"]["time"] = year

        if year > current_year:
            current_year = year
            print(current_year)
            print(magnitude)
            mag = []
            mag.append(magnitude)
            data[str(year)] = mag
        else:
            mag_list = data[str(year)]
            mag_list.append(mag_list)

    data_averages= []
    data_years = []
    for year in data.keys():
        mag_list = data[year]
        average_magnitude = np.average(mag_list)
        data_averages.append(average_magnitude)
        data_years.append(year)

    return data_averages, data_years

def map_at(*args, **kwargs):
    return request_map_at(*args, **kwargs).content

def main():
    # getting earthquake data from URL
    quakes = get_data()
    # parsing data
    earthquake_data = json.loads(quakes.text)
    # extracting features from data (where earthquake mag and coordinates located)
    features = earthquake_data["features"]
    # looking for coordinates where max magnitude occurs
    max_mag, coord_max_mag = max_magnitude(features)
    # generating URLs for map
    for coordinate in coord_max_mag:
        map_response = request_map_at(coordinate[0], coordinate[1])
        url = map_response.url
        print(url[0:])
        # Displaying image
        map_png = map_at(*coordinate)
        Image(map_png)
    # Calculating average magnitude per year
    average_magnitude,years = avg_mag(features)

    plt.bar(average_magnitude,years)
    plt.ylabel('average magnitude')
    plt.xlabel('year')
    plt.show()

    print(average_magnitude)

    print(f"The maximum magnitude is {max_mag} "
          f"and it occured at coordinates {coord_max_mag}.")


if __name__ == "__main__":
    main()
