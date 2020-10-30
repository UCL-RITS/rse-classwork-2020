import requests
import json
import numpy as np 
from datetime import datetime
import matplotlib.pyplot as plt

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
quakes = requests_json['features']

times = [q['properties']['time'] for q in quakes]

timeList = []
for t in times:
    timeList.append(int(datetime.fromtimestamp(t/1000).strftime("%Y")))

dates = np.unique(timeList)

numList = []   
means = []
for d in dates:
    mags = []
    numList.append(timeList.count(d))
    for t in timeList:
        if t == d:
            mags.append([q['properties']['mag'] for q in quakes])
    means.append(np.mean(mags))


plt.figure()
plt.bar(dates, numList)
plt.xlabel('Year')
plt.ylabel('Number of Quakes')
plt.title('Frequency of Earthquakes By Year')

plt.figure() 
plt.bar(dates, means)
plt.xlabel('Year')
plt.ylabel('Average Quake Magnitude')
plt.title('Average Quake Magnitude By Year')

plt.show()

print(means)