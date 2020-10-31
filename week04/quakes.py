"""A script to find the biggest earthquake in an online dataset."""
import requests
import datetime
import json
import matplotlib
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

quake_data = json.loads(quakes.text)

max_magnitude = 0

print('There are',len(quake_data['features']),'earthquakes in this dataset.')

frequency = {} # empty frequency dictionary
magnitude = {} # empty magnitude dictionary

for quake in quake_data['features']:
    year = datetime.datetime.fromtimestamp(quake['properties']['time']/1000.0).year

    # counting number of earthquakes (frequency) within a year
    if year in frequency:
        frequency[year] = frequency[year] + 1
    else:
        frequency[year] = 1

    # average magnitude of earthquakes within a year
    if year in magnitude:
        magnitude[year] = magnitude[year] + quake['properties']['mag']
    else:
        magnitude[year] = quake['properties']['mag']
        
    if quake['properties']['mag'] > max_magnitude:
        max_magnitude = quake['properties']['mag']
        title = quake['properties']['title']
        coords = quake['geometry']['coordinates']
        time = datetime.datetime.fromtimestamp(quake['properties']['time']/1000.0)
        updated = datetime.datetime.fromtimestamp(quake['properties']['updated']/1000.0)

# average magnitude / year
for year in magnitude:
    magnitude[year] = magnitude[year] / frequency[year]

print("The earthquake with the largest magnitude was:",max_magnitude,"in",title,"with the location",coords,"at time",time,"and updated at",updated,".")
# print(frequency)

# figure 1 - frequency
plt.figure(figsize = (12,5))    
plt.title('Frequency of Quakes per Year')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.bar(range(len(frequency)),list(frequency.values()),align='center')
plt.xticks(range(len(frequency)),list(frequency.keys()))

# figure 2 - average magnitude
plt.figure(figsize = (12,5))    
plt.title('Average Magnitude per Year')
plt.xlabel('Year')
plt.ylabel('Average Magnitude')
plt.bar(range(len(magnitude)),list(magnitude.values()),align='center')
plt.xticks(range(len(magnitude)),list(magnitude.keys()))

plt.show()
