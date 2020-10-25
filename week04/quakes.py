"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json

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
                          "endtime": "2020-10-25",
                          "orderby": "time-asc"}
                      )
#initialize variables for the loop
max_magnitude = 0
coords = ''

#loop around the structure
for items in quakes.json()["features"]:
    events = items['properties']
    geometries = items['geometry']
    if events['mag'] > max_magnitude:
        # new biggest magnitude - reset variables
        max_magnitude = events['mag']
        coords= geometries['coordinates']  
        

    # The results are stored in variables
    # named max_magnitude and coords,

print(f"The maximum magnitude is {max_magnitude} "
      f"and it occured at coordinates {coords}.")
