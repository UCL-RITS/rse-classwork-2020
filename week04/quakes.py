"""A script to find the biggest earthquake in an online dataset."""
import requests
import json



if __name__ == "__main__":
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


    my_request = json.loads(quakes.text)
    largest_quake = quake_feature[0]
    
    for quake in quake_feature:
        if quake['properties']['mag'] > largest_quake['properties']['mag']:
            largest_quake = quake
    max_magnitude = largest_quake['properties']['mag']
    coords= largest_quake['geometry']['coordinates'][0],largest_quake['geometry']['coordinates'][1]
    
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
