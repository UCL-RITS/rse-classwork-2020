import json
import requests
from datetime import date
from datetime import datetime
from matplotlib import pyplot as plt


# retrieve the data
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

# parse the json data
raw_data = json.loads(quakes.text) 
qdata = raw_data["features"] 

# list comprehension used to find the maximum magnitude and the corresponding coordinates
max_magnitude = max([x["properties"]["mag"] for x in qdata])
coords= [x["geometry"]["coordinates"] for x in qdata if x["properties"]["mag"]==max_magnitude]

# retrieve the year for each earthquake
date_list=[date.fromtimestamp(x["properties"]["time"]/1000.0).year for x in qdata]

# track the number of frequency for each year
quake_dict = {i:date_list.count(i) for i in date_list}

# define the lists for the axes
x_axis = list(quake_dict.keys())
y_axis = [x for x in quake_dict.values()]

# plot and format the graph
freq_graph, freq_graph_axes = plt.subplots()
freq_graph_axes.bar(x_axis, y_axis)
freq_graph_axes.set_title("Plot of earthquake frequency against year")
freq_graph_axes.set_ylabel("Frequency")
freq_graph_axes.set_xlabel("Year")
freq_graph

