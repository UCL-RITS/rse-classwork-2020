import matplotlib.pyplot as plt 
import requests
import json 
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
type(requests_json)

print(requests_json.keys())

times = []

# for every earthquake in the dataset
Nquakes = len(requests_json['features'])

for q in range(Nquakes):
  t_quake = requests_json['features'][q]['properties']['time'] / 1000 # in ms
  times.append(
        datetime.datetime.fromtimestamp(t_quake).strftime('%Y-%m-%d %H:%M:%S')[:4]
      ) 

plt.figure(figsize=(12,6))
plt.hist(times)
plt.ylabel('frequency')
plt.xlabel('years')
plt.show()

magnitudes = []

# for every earthquake in the dataset
Nquakes = len(requests_json['features'])

for q in range(Nquakes):
  mag_quake = requests_json['features'][q]['properties']['mag']
  magnitudes.append(mag_quake) 

plt.figure(figsize=(12,6))
plt.hist(magnitudes)
plt.xlabel('magnitudes')
plt.ylabel('frequency')
plt.text(0.7,0.7,'')
plt.show()