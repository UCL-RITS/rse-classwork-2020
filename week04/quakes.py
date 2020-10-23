import datetime
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
                          "endtime": "2020-10-23",
                          "orderby": "time-asc"}
                      )

data = json.loads(quakes.text)

max_magnitude = 0
coords = []
time = []

for earthquake in data['features']:
    if earthquake['properties']['mag'] > max_magnitude:
        max_magnitude = earthquake['properties']['mag']
        coords = earthquake['geometry']['coordinates']
        time = datetime.datetime.fromtimestamp(earthquake['properties']['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
    elif earthquake['properties']['mag'] == max_magnitude:
        coords = [coords, earthquake['geometry']['coordinates']]
        time = [time, datetime.datetime.fromtimestamp(earthquake['properties']['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')]

print(f"The maximum magnitude is {max_magnitude} "
      f"and it occured at coordinates {coords} "
      f"on {time}.")