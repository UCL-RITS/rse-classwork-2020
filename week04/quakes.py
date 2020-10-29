
import json
import requests
import numpy as np
import pandas as pd
import inflect
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats

# We use inflect to convert 1 into "1st", 2 into "2nd" etc
integer_engine = inflect.engine()


###################################################################
# This code is split into 3 sections
#    1. Download data and parse it
#    2. Find and print strongest earthquakes
#    3. Plot details of earthquake size and mean magnitude by year
###################################################################

###################################################################
## Section 1 - load data and parse it into a dataframe
###################################################################

# Load the data from the USGS earthquake service
quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": datetime.today().strftime('%Y-%m-%d'),
                          "orderby": "time-asc"}
                      )

# Convert the result into a dictionary
quakes_object = json.loads(quakes.text)

# Now convert all the earthquakes into a pandas dataframe
quakes_dataframe = pd.json_normalize(quakes_object['features'])

###################################################################
## Section 2 - find and print strongest earthquakes
###################################################################

# Get the row in the dataframe that corresponds to the strongest quake
max_quake = quakes_dataframe[quakes_dataframe['properties.mag'] == quakes_dataframe['properties.mag'].max()]

# Reset the index so the row numbers start from 0
max_quake = max_quake.reset_index(drop=True)

# Print all the strongest earthquakes
for index, quake in max_quake.iterrows():
    # Print the strongest earthquake
    print(f"The maximum magnitude is {quake['properties.mag']} "
          f"and it occured for the {integer_engine.ordinal(index + 1)} time at ({', '.join(str(x) for x in quake['geometry.coordinates'][0:2])}) at {quake['geometry.coordinates'][2]} kilometres deep.")

###################################################################
## Section 3 - plot by year, the number and mean quake magnitude
###################################################################

# Convert milisecond unix timestamp to datetime
quakes_dataframe['properties.time'] = quakes_dataframe['properties.time'].apply(lambda x: datetime.fromtimestamp(x/1000))

# Group by year and get the mean magnitude and number of magnitudes
yearly_quakes = quakes_dataframe['properties.mag'].groupby(quakes_dataframe['properties.time'].dt.year).agg(['mean', 'count', stats.sem])

# Get list of years
years = yearly_quakes.index.tolist();

# Take every 5th year for ticks
xtick_years = np.append(np.arange(np.min(years), np.max(years), step=5), np.max(years))

# Plot mean magnitude of quakes each year
f = plt.figure()
plt.errorbar(years, yearly_quakes['mean'], yearly_quakes['sem'], capsize=3)

# Configure axes
plt.xticks(xtick_years)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Mean magnitude (Richter)', fontsize=16)

# Show, and save as PDF
plt.show()
f.savefig("quake_magnitude_by_year.pdf", bbox_inches='tight')

# Plot number of quakes per year
f = plt.figure()
plt.plot(years, yearly_quakes['count'])

# Configure axes
plt.xticks(xtick_years)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Number of quakes', fontsize=16)

# Show, and save as PDF
plt.show()
f.savefig("quake_count_by_year.pdf", bbox_inches='tight')
