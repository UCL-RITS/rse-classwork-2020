import requests
quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}    ).text
import json 
json.dumps(quakes)
with open('quakes.json') as json_quakes_in:
    quakes_again = json.load(json_quakes_in)

new_dict = {key: val for key, val in quakes_again.items() if val > 2}