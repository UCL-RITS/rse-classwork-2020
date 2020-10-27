import requests
import datetime
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
                          "orderby": "time-asc"}    )
quakes_json_data = json.loads(quakes.text)

max_mag = max(quake['properties']['mag'] for quake in quakes_json_data['features'])

for feature in quakes_json_data['features']:
        if feature['properties']['mag'] == max_mag:
            quake_coord = feature['geometry']['coordinates']

print('The large magnitude earthquake was: ',max_mag, 'located at the coordinates', quake_coord)