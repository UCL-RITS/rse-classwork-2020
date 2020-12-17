"""Producing Plots for the Quakes Dataset"""

#1.plot the frequency of earthquakes per year
#2.plot the average magnitude of earthquakes per year

from datetime import date
import requests
import json
import statistics

import matplotlib.pyplot as plt
import numpy as np

# Defining this function is not necessary, but it helps make the subsequent
# analysis shorter and more readable, because we give an indication of what
# this code does.
def process_earthquake(data):
    """Extract the year and magnitude from an earthquake record."""
    timestamp = data['properties']['time']
    year = date.fromtimestamp(timestamp/1000).year
    return year, data['properties']['mag']

# Get the data we will work with
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

# Get the year and magnitude of each earthquake
years_magnitudes = [process_earthquake(feature) for feature in quakes]

# Compute the number of earthquakes per year and their magnitudes

# Option 1: loop through results and see how many times we encounter each year
# Note that this could also be done in two stages, one for the frequencies
# and one for the magnitudes.
magnitudes_per_year = {}    # creates an empty dictionary
for year, mag in years_magnitudes:
    if year not in magnitudes_per_year:  # if we haven't seen this year before, add it
        magnitudes_per_year[year] = [mag]
    else:  # otherwise record one more instance
        magnitudes_per_year[year].append(mag)
# Convert to lists for plotting
# Note that we have to ensure the same ordering in both lists! This is one way:
years = sorted(magnitudes_per_year.keys())
numbers = [len(magnitudes_per_year[year]) for year in years]
magnitudes = [  # the statistics module has some basic statistical functions
    statistics.mean(magnitudes_per_year[year])
    for year in years
]

# Option 2: use numpy for the computations
years_only = [y for y, m in years_magnitudes]
years, numbers = np.unique(years_only, return_counts=True)
# Note that unique returns the years in ascending order already!
magnitudes = [
    np.mean([m for y, m in years_magnitudes if y == year])
    for year in years
]

# Plot the results - this is not perfect since the x axis is shown as real
# numbers rather than integers, which is what we would prefer!
plt.bar(years, numbers)
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Number of earthquakes per year")
plt.savefig("frequencies.png")  # Save the figure to a file
plt.clf()  # This clears the figure, so that we don't overlay the two plots

plt.plot(years, magnitudes)
plt.xlabel("Year")
plt.ylabel("Magnitude")
plt.title("Average earthquake magnitude per year")
plt.savefig("average_magnitudes.png")