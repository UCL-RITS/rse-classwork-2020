"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "1901-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2000-12-31",
                          "orderby": "time-asc"}
                      )
    # parsing the data as JSON
    quakes_json = json.loads(quakes.text)
    # obtaining a list of earthquake magnitudes
    mag_list = [quakes_json['features'][i]['properties']['mag'] for i in range(quakes_json['metadata']['count'])] 
    # finding the maximum earthquake magnitude
    max_mag = max(mag_list)
    # findng the index corresponding to maximum earthquake magnitude
    max_mag_pos = [ i for i in range(len(mag_list)) if mag_list[i] == max_mag] 
    # finding the coordinates corresponding to maximum earthquake magnitude
    coordinates_max = [quakes_json['features'][max_mag_pos[i]]['geometry']['coordinates'] for i in range(len(max_mag_pos))]
        
    print(f"There is {len(max_mag_pos)} event(s) with a maximum magnitude of {max_mag}")
    print("These event(s) occured at coordinates:", {(coordinates_max[i][0],coordinates_max[i][1]) for i in range(len(coordinates_max))})
