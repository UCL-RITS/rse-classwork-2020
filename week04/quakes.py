"""A script to find the biggest earthquake in an online dataset."""
import requests
import json
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