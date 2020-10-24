"""A script to find the biggest earthquake in an online dataset."""

import requests
import json

if __name__ == "__main__":
    # We first load the data 
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

    # Writing the data in a readable format
    json_data = json.loads(quakes.text)

    # We now find the relevant data and use it to search for the maximum magnitude
    quakes_data = json_data['features']
    magnitudes = []
    for quake in quakes_data:
        quake_magnitude = quake['properties']['mag']
        magnitudes.append(quake_magnitude)
    max_magnitude = max(magnitudes)
    
    # We now look for where this maximum magnitude earthquakes happened
    coords = []
    for quake in quakes_data:
        if quake['properties']['mag'] == max_magnitude:
            coord = quake['geometry']['coordinates']
            coords.append(coord)
            
    # Printing the solution found
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
