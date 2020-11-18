"""A script to find the biggest earthquake in an online dataset."""
import json
import requests

if __name__ == "__main__":

    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "1900-01-01", 
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )
    print(quakes.text[0:100])

    # Save request in json file for exploration
    json_data = json.loads(quakes.text)
    with open("quakes.txt", "w") as f:
        json.dump(json_data,f, indent = 4)


    quake_data = json_data['features']
    max_magnitude = max([quake['properties']['mag'] for quake in quake_data])
    coords = [quake['geometry']['coordinates'] for quake in quake_data if quake['properties']['mag'] == max_magnitude]

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
