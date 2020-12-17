"""A script to find the biggest earthquake in an online dataset."""

import json
import requests

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



earthquakesjson=json.loads(quakes.text)

listofquakes=earthquakesjson['features']

largestquake = listofquakes[0] #says the largest quake we have seen so far is the first one
for i in listofquakes:
    if i['properties']['mag'] > largestquake['properties']['mag']:
        largestquake=i


lmag=largestquake['properties']['mag']
llat=largestquake['geometry']['coordinates'][1]
llong=largestquake['geometry']['coordinates'][0]
coords=[llat,llong]

print(f"The maximum magnitude is {lmag} " ,f"and it occured at coordinates {coords}.")
