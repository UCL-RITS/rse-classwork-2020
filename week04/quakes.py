import requests
import json
import time 
import datetime
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

quakes = json.loads(quakes.text)
print(quakes['features'][0]['properties'].keys())

max_mag = 0
max_quake = None
num_quakes = len(quakes['features'])
for f in quakes['features']:
    if f['properties']['mag'] > max_mag:
        max_mag = f['properties']['mag']
        max_quake = f


year_list = []
mag_dict = {}
years = []
mag_avg = []

for f in quakes['features']:
    t = f['properties']['time']
    mag = f['properties']['mag']
    year = datetime.datetime.fromtimestamp(t/1000).year
    year_list.append(year)

    if year in mag_dict.keys():
        mag_dict[year].append(mag)
    else:
        mag_dict[year] = [mag]

for k in mag_dict.keys():
    years.append(k)
    mag_avg.append(sum(mag_dict[k])/len(mag_dict[k]))

plt.hist(year_list, bins=18)
plt.xticks(range(min(year_list), max(year_list)+1))
plt.xlabel('year')
plt.ylabel('frequency')
plt.show()
print(year_list)

plt.plot(years, mag_avg)
plt.xticks(range(min(year_list), max(year_list)+1))
plt.xlabel('year')
plt.ylabel('Average Magnitude')
plt.show()

print(max_mag)
print(max_quake)

print("The biggest quake was in %s (%s), with Mag %s" % (max_quake['properties']['place'],
max_quake['geometry']['coordinates'], max_quake['properties']['mag']))
print("https://www.google.com/maps/search/?api=1&query=%s,%s" % (max_quake['geometry']['coordinates'][1], 
max_quake['geometry']['coordinates'][0]))