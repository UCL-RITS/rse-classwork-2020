"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import json
import requests
import datetime

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
requests_json = json.loads(quakes.text)
all_eq_dicts = requests_json['features']
print(requests_json['features'][0]['properties']['time'])

print(len(all_eq_dicts))
mags, titles, lons, lats, times = [], [], [], [],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    time = eq_dict['properties']['time']
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    times.append(time)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
print(times[:5])
# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
#if __name__ == "__main__":
    # ...do things here to find the results...
    
    #quakes_info = quakes.text
    #print(quakes.text)
    #filename = 'quakes_data.json'
    #with open(filename, 'w') as f:
        #json.dump(quakes_info , f)
    #with open(filename) as f:
        #magnitude_info = json.load(f)

    #list_magnitude = magnitude_info['minmagnitude']
    #print(max(list_magnitude))

    #max_magnitude   
    #coords
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    #print(f"The maximum magnitude is {max_magnitude} "
    #      f"and it occured at coordinates {coords}.")
