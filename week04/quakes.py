"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...
import json
import requests
import datetime
import matplotlib.pyplot as plt
from collections import Counter

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...
   quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "1920-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2019-12-31",
                          "orderby": "time-asc"}
                      )
quake_data = json.loads(quakes.text)
#print(json.dumps(quake_data, indent = 4))

magnitude=[]
times=[]
for quake in quake_data['features']:
    magnitude.append(quake['properties']['mag'])
    time=datetime.datetime.fromtimestamp(quake['properties']['time']/1000).strftime('%Y')
    times.append(time)
    
max_magnitude = max(magnitude)
index = magnitude.index(max_magnitude)  
coords = quake_data['features'][index]['geometry']['coordinates']
place = quake_data['features'][index]['properties']['place']

q = Counter(times)


plt.plot(q.keys(), q.values())
plt.title('Number of quakes per year')
plt.xlabel("Year")
plt.ylabel("Number of quakes")

plt.show()



#print(times)
    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords} in {place}.")


