"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import requests
import json
import numpy as np

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
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
    
    json_quakes = json.loads(quakes.text)
    n_quakes = len(json_quakes['features'])
    
    tot_mags = np.zeros(n_quakes)
    tot_coords = np.zeros([n_quakes,3])

    for i in range (n_quakes):
        mag = json_quakes['features'][i]['properties']['mag']
        coord = json_quakes['features'][i]['geometry']['coordinates']

        tot_mags[i] = mag
        tot_coords[i] = coord


    max_locs = np.where(tot_mags == max(tot_mags))
    
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print('Locations of biggest earthquakes')
    for i in max_locs[0]:
        print('Location '+str(i))
        print('Magnitude : '+str(tot_mags[i]) )
        print('Coordinates : '+str(tot_coords[i]))
        print('Location description : '+ json_quakes['features'][i]['properties']['place'])
