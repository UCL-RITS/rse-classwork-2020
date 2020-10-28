"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import requests

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
f = open("quakes.txt", "a")
f.write(quakes.text)
f.close()

import json
with open('quakes.txt', 'r') as source:
         quakes_dict = json.loads(source.read())
with open('Data.json','w') as output2:
     json.dump(quakes_dict,output2)
# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
N = len(quakes_dict['features'])
mag = quakes_dict['features'][0]['properties']['mag']
coord = []
for key in range(0,N):
    mag_new = quakes_dict['features'][key]['properties']['mag']
    if mag_new > mag:
        mag = mag_new
        coord = quakes_dict['features'][key]['geometry']['coordinates']
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
print('The maximum magnitude is ', mag,' and it occured at coordinates ',coord)

