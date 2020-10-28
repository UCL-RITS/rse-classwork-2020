import requests
import json
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
#firstly we write the quakes data to a txt file                      
with open('quake_data.txt', 'w') as my_input:
    my_input.write(quakes.text[:])

# Then, we read the data from file and we store them 
with open('quake_data.txt', 'r') as source:
    quake_data = json.loads(source.read())

#find the maximum magnitude
quakes_data = quake_data['features']
max_magnitude = 0
for quake in quakes_data:
    magnitude = quake['properties']['mag']
    if magnitude > max_magnitude:
        max_magnitude = magnitude
coords = []
place = ""
for quake in quakes_data:
    if quake['properties']['mag'] == max_magnitude:
        coords.append(quake['geometry']['coordinates'])
        place = quake['properties']['place']    
print(f"The maximum magnitude is {max_magnitude} "+
        f"happened in {place}"
        f"and it occured at coordinates {coords}.")