"""A script to find the biggest earthquake in an online dataset."""
import json
import requests

# At the top of the file, import any libraries you will use.
# import ...

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...

    # retrieve the json data
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson", params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"})

    # parse the json data
    raw_data = json.loads(quakes.text) 
    qdata = raw_data["features"] 

    # list comprehension used to find the maximum magnitude and the corresponding coordinates
    max_magnitude = max([x["properties"]["mag"] for x in qdata])
    coords= [x["geometry"]["coordinates"] for x in qdata if x["properties"]["mag"]==max_magnitude]


    # display the results
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
