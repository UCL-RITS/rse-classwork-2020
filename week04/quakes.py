"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import requests

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...
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
f = open("quakes.txt", "a")
f.write(quakes.text)
f.close()

import json
with open('quakes.txt', 'r') as source:
         quakes_dict = json.loads(source.read())
with open('Data.json','w') as output2:
     json.dump(quakes_dict,output2)
# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
N = len(quakes_dict['features'])
mag = quakes_dict['features'][0]['properties']['mag']
coord = []
for key in range(0,N):
    mag_new = quakes_dict['features'][key]['properties']['mag']
    if mag_new > mag:
        mag = mag_new
        coord = quakes_dict['features'][key]['geometry']['coordinates']
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
print('The maximum magnitude is ', mag,' and it occured at coordinates ',coord)

# Re-format the time

import datetime

year_plt = []
mag_dict = {}

for data in quakes_dict['features']:
    time = data['properties']['time']
    dt_obj = datetime.datetime.fromtimestamp(time/1000)
    year = dt_obj.year
    year_plt.append(year)
    
    # Create dict to collect magnitude in each year. 
    # Year is a key. Mag is a value.
    mag = data['properties']['mag']
    if year in mag_dict.keys():
        mag_dict[year].append(mag)
    else:
        mag_dict[year] = [mag]
    
#print(year_plt)
#print(mag_dict)

# Calculate the average magnitude each year
year_final = []
mag_mean = []
freq = []
for i in mag_dict.keys():
    year_final.append(i)
    avg = sum(mag_dict[i])/len(mag_dict[i])
    mag_mean.append(avg)
    freq.append(len(mag_dict[i]))
#print(year_final)
#print(mag_mean)
#print(freq)

## Plot data
from matplotlib import pyplot as plt

plt.plot(year_final, mag_mean)
plt.xlabel('Year')
plt.ylabel('Average magnitude')

plt.bar(year_final, freq)
plt.xlabel('Year')
plt.ylabel('Frequency')

