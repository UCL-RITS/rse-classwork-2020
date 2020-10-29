"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...

import yaml
import requests

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

quakes_file=yaml.safe_load(quakes.text)
quakes_features=quakes_file['features']

k=len(quakes_features)
current_place=[]
current_mag=[]
each_quake=[]
current_coord=[]

for i in range(k):

    each_quake=quakes_features[i]
    
    current_place+=[each_quake['properties']['place']]
    current_mag+=[each_quake['properties']['mag']]
    current_coord+=[each_quake['geometry']['coordinates']]

biggest=max(current_mag)
chosen=[]
big_coo=[]

for i in range(k):
    if biggest==current_mag[i]:
        chosen+=[i]
        big_coo.append(current_coord[i])
        
print(f"The maximum magnitude is {biggest} "
f"and it occured at coordinates {big_coo}.")


# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
# if __name__ == "__main__":
#     # ...do things here to find the results...



