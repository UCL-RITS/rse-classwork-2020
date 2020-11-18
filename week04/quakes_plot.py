import requests
import json
import numpy as np
import matplotlib.pyplot as plt

def find_year(date_in_ms):
    years_since_start=date_in_ms/(1000.0*31556926.0)
    return int(years_since_start+1970)

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
                      ).text

    with open('quakes_data.json' ,'w') as quakes_data_file:
        quakes_data_file.write(quakes)

    with open('quakes_data.json','r') as quakes_source:
        quakes_content = quakes_source.read()

    quakes_data = json.loads(quakes_content)

    times_in_ms = [i['properties']['time'] for i in quakes_data['features']]
    magnitudes = [i['properties']['mag'] for i in quakes_data['features']]
    years = [find_year(i) for i in times_in_ms]

    max_year = max(years)
    min_year = min(years)

    earthquakes_per_year = {}
    average_quake_mag_per_year = {}
    for j in np.arange(min_year,max_year+1,1):
        earthquakes_per_year[j] = 0
        average_quake_mag_per_year[j] = 0

    for year in years:
        earthquakes_per_year[year] += 1
        



    quakes_frequency = [i for i in earthquakes_per_year.values()]
    quakes_date = [int(i) for i in earthquakes_per_year.keys()]

    plt.bar(quakes_date, quakes_frequency)
    plt.title('Frequency of Earthquakes per year')
    plt.xlabel('year')
    plt.ylabel('No of quakes')

    plt.show()


