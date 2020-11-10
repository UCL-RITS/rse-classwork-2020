"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json
# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...

    max_magnitude = 0
    coords = {}
    
    # this block of code gets the data of all the earthquakes that occured in UK in the last century (1900-1999)
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "1900-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "1999-12-31",
                          "orderby": "time-asc"}
                      )
                    
    # We write the above data in a txt file (quake_data.txt)
    with open('quake_data.txt', 'w') as target:
        target.write(quakes.text[:])

    # Then, we read the data from file and we store them to a variable (of type dictionary) named quake_data_dict
    with open('quake_data.txt', 'r') as source:
        quake_data_dict = json.loads(source.read())

    # a loop that compares every earthquake's magnitute with the maximum magnitude
    # if miximum magnitude is found, then the max_magnitude and coords variables are updated.
    for item in quake_data_dict['features']:
        if item['properties']['mag'] == max_magnitude:
            coords['coords'].append(item['geometry']['coordinates'][0:2]) # if more than one location exists with the maximum magnitude
        elif item['properties']['mag'] > max_magnitude: # if a location has a magnitude bigger than the max_magnitude
            coords['coords'] = [item['geometry']['coordinates'][0:2]] #coords is a dictionary so we store the value approprietly
            max_magnitude = item['properties']['mag']
            

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords['coords']}.")

