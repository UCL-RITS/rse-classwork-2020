"""A script to find the biggest earthquake in an online dataset."""

import requests
import json
from datetime import date
import copy
from matplotlib import pyplot as plt
import numpy as np

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

quakes_json = json.loads(quakes.text)
# with open('quakes.json', 'w') as file:
#     json.dump(quakes_json, file)
quakes_lst = quakes_json['features']

quake_yrs = [ date.fromtimestamp(quake['properties']['time']/1000).year for quake in quakes_lst ]
quake_mags = { yr : np.mean([ quake['properties']['mag'] for quake in quakes_lst if date.fromtimestamp(quake['properties']['time']/1000).year == yr]) for yr in quake_yrs }

fig, axs = plt.subplots(1, 2)

axs[0].hist(quake_yrs)
axs[0].set_ylabel('frequency')
axs[0].set_xlabel('yr')

axs[1].plot(quake_mags.keys(), quake_mags.values())
axs[1].set_ylabel('avg_mag')
axs[1].set_xlabel('yr')

plt.tight_layout()
plt.show()

max_mag = max([ quake['properties']['mag'] for quake in quakes_lst ])
max_mag_idx = [ idx for idx, val in enumerate([ quake['properties']['mag'] for quake in quakes_lst ]) if val == max_mag ]
max_mag_coords = [ quakes_lst[i]['geometry']['coordinates'] for i in max_mag_idx ]

print('The maximum magnitude of a quake in the UK in the past century has been a ' + str(max_mag) + '. It has occured ' + str(len(max_mag_coords)) + ' times at the coordinates ' + str(max_mag_coords))
