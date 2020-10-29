"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...

import json
import requests
import datetime
import matplotlib.pyplot as plt

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
                          'starttime': "1900-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2020-10-11",
                          "orderby": "time-asc"}
                      )
    
    df = json.loads(quakes.text)
    quakes_data = df['features']
    max_magnitude = 0
    coords = []

    for quake in quakes_data:
        magnitude = quake['properties']['mag']
        if magnitude > max_magnitude:
            max_magnitude = magnitude

    for quake in quakes_data:
        if quake['properties']['mag'] == max_magnitude:
            coords.append(quake['geometry']['coordinates'])
    
    quakes_by_year = {}
    
    for quake in quakes_data:
        time = quake['properties']['time']
        time = datetime.datetime.fromtimestamp(time/1000)
        if time.year not in quakes_by_year:
            quakes_by_year[time.year] = {"number": 0, "magnitude_average": 0}
        quakes_by_year[time.year]["number"] +=1
        quakes_by_year[time.year]["magnitude_average"] = (quakes_by_year[time.year]['magnitude_average'] \
                                                        * (quakes_by_year[time.year]["number"] -1) \
                                                        + (quake['properties']['mag'])) \
                                                            / (quakes_by_year[time.year]["number"])
    
    x = [k for k in quakes_by_year]
    y = [k["number"] for k in quakes_by_year.values()]
    z = [k["magnitude_average"] for k in quakes_by_year.values()]
    print(z)

    fig, axs = plt.subplots(2, sharex=True)
    axs[0].plot(x,z)
    axs[1].plot(x,y)
    axs[0].set_ylabel("Average Magnitude")
    axs[1].set_ylabel("Frequency")
    axs[1].set_xlabel("Year")

    plt.savefig("Quakes_Data_Viz.png")





    


    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")