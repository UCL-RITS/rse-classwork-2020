import json
import requests
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01", 
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime":"2018-10-11",
                          "orderby": "time-asc"}
                      )
    print(quakes.text[0:100])


    json_data = json.loads(quakes.text)
    quake_data = json_data['features']

    
    years = []
    year_list = range(2000,2019)
    for year_val in year_list:
        years.append(1000*time.mktime(datetime.datetime.strptime(str(year_val)+"-01-01", "%Y-%m-%d").timetuple()))
    
    quake_time =  [quake['properties']['time'] for quake in quake_data]


    plt.figure()
    plt.hist(quake_time, years)
    plt.show()