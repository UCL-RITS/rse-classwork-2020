"""A script to plot average earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json
import datetime
import time
import matplotlib.pyplot as plt

#constants
START = 2000  # start year = need to align to selection below
POINTS = 21   # number of years considered
STARTTIME = "2000-01-01" # Start time in string format
ENDTIME = "2020-12-31"   # End time in string format

# When you run the file, it should graph the average magnitude of quakes by year.
# You can run the file with `python graphs.py` from this directory.
if __name__ == "__main__":
    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': STARTTIME,
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": ENDTIME,
                          "orderby": "time-asc"}
                      )

#define and initialise lists
years = [x+ START for x in range(POINTS)]
counts = [0 for x in range(POINTS)]
mags = [0 for x in range(POINTS)]
averages = [0 for x in range(POINTS)]
#loop around the whole structure
#find year and update count and mags
for items in quakes.json()["features"]:
    events = items['properties']
    timestring = time.gmtime(events['time']/1000)
    year = (time.strftime("%Y ", timestring))
    int_year = int(year)
    index = int_year - START
    counts[index] = counts[index]+1
    mags[index] = mags[index]+events['mag']

# calculate average from counts
for i in range(POINTS):
    if counts[i]>0:
        averages[i] = mags[i]/counts[i]

plt.plot(years, averages, 'ro')
plt.style.use('ggplot')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Earthquake analysis by year')
plt.show()
