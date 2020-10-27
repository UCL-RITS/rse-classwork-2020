"""A script to find the biggest earthquake in an online dataset."""

week04

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
                          "orderby": "time-asc"}
                      )

quake_data = json.loads(quakes.text)

max_magnitude = 0

for quake in quake_data['features']:
    if quake['properties']['mag'] > max_magnitude:
        max_magnitude = quake['properties']['mag']
        title = quake['properties']['title']
        coords = quake['geometry']['coordinates']
        time = datetime.datetime.fromtimestamp(quake['properties']['time']/1000.0)
        updated = datetime.datetime.fromtimestamp(quake['properties']['updated']/1000.0)

print("The earthquake with the largest magnitude was:",max_magnitude,"in",title,"with the location",coords,"at time",time,"and updated at",updated,".")
