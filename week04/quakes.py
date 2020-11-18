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
                      ).text

    with open('quakes_data.json' ,'w') as quakes_data_file:
        quakes_data_file.write(quakes)

    with open('quakes_data.json','r') as quakes_source:
        quakes_content = quakes_source.read()

    quakes_data = json.loads(quakes_content)

    magnitudes = [i['properties']['mag'] for i in quakes_data['features']]

    max_magnitude = max(magnitudes)

    coords_finder = (i['geometry']['coordinates'] for i in quakes_data['features'] \
    if i['properties']['mag'] == max_magnitude)

    coords = [xyz for xyz in coords_finder]

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
