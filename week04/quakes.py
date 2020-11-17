"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import requests
import json

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

    # Load the data
# quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
#                       params={
#                           'starttime': "2000-01-01",
#                           "maxlatitude": "58.723",
#                           "minlatitude": "50.008",
#                           "maxlongitude": "1.67",
#                           "minlongitude": "-9.756",
#                           "minmagnitude": "1",
#                           "endtime": "2018-10-11",
#                           "orderby": "time-asc"}
#                       )
# #quakes.text[0:100]
# requests_json = json.loads(quakes.text)

# with open("quakes.json","w") as f:
#     json.dump(requests_json,f,indent = 4)

try:
    with open("quakes.json","r") as f:
        requests_json = json.load(f)
except FileNotFoundError:
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
    #quakes.text[0:100]
    requests_json = json.loads(quakes.text)

    with open("quakes.json","w") as f:
        json.dump(requests_json,f,indent = 4)


#print(requests_json['features'][0])
#print(requests_json.keys())
#print(len(requests_json['features']))
#print(requests_json['features'][0]['properties']['mag'])

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    quakes = requests_json['features']
    #max_magnitude = max(index['properties']['mag'] for index in quake)
    '''
    for index in range(120):
        max_magnitude = max([quakes[index]['properties']['mag']])
    '''
    max_magnitude = max([quakes[index]['properties']['mag'] for index in range(120)])



    coords = [index['geometry']['coordinates'] for index in quakes if index['properties']['mag'] == max_magnitude]


    '''wrong solution - only one coordinate is achieved
    max_magnitude = requests_json['features'][0]['properties']['mag']
    coords = requests_json['features'][0]['geometry']['coordinates']
    for index in range(120):
        if requests_json['features'][index]['properties']['mag'] > max_magnitude:
            max_magnitude = requests_json['features'][index]['properties']['mag']
    
            coords = requests_json['features'][index]['geometry']['coordinates']
    '''
    
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")