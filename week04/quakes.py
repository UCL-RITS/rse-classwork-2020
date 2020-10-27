
import json
import requests
import numpy as np
import pandas as pd
import inflect
from datetime import datetime

# We use inflect to convert 1 into "1st", 2 into "2nd" etc
integer_engine = inflect.engine()

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

# Get the row in the dataframe that corresponds to the strongest quake
max_quake = quakes_dataframe[quakes_dataframe['properties.mag'] == quakes_dataframe['properties.mag'].max()]

# Reset the index so the row numbers start from 0
max_quake = max_quake.reset_index(drop=True)

# Print all the strongest earthquakes
for index, quake in max_quake.iterrows():
    # Print the strongest earthquake
    print(f"The maximum magnitude is {quake['properties.mag']} "
          f"and it occured for the {integer_engine.ordinal(index + 1)} time at ({', '.join(str(x) for x in quake['geometry.coordinates'][0:2])}) at {quake['geometry.coordinates'][2]} kilometres deep.")
