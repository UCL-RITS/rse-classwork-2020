"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
from IPython.display import Image

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
    quakes_json = quakes.json()
    features = quakes_json["features"]
    n = len(features)
    temp_mag = float(0)
    temp_i = 0
    for i in range(n):
        try:
            if features[i]["properties"]["mag"]>temp_mag:
                temp_mag = features[i]["properties"]["mag"]
                temp_i = i
        except:
            pass
    max_magnitude = features[temp_i]["properties"]["mag"]
    coords = features[temp_i]["geometry"]["coordinates"]

    url = "https://static-maps.yandex.ru/1.x/?z=10&size=400,400&ll=" + str(coords[0]) + "," + str(coords[1]) + "&l=map" + "&lang=en_US"
    img = requests.get(url)
    Image(img.content)
    
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
