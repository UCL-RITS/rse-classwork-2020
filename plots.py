import matplotlib.pyplot as plt
import requests
import json

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

data = json.loads(quakes.text)

def date_qualifies(ms_since_1970):
    years_since_1970 = 1970 + (ms_since_1970 / (1000 *3600 * 24 * 365))
    if years_since_1970  > 2000:
        return True, int(years_since_1970)
    else:
        False, int(years_since_1970)

def get_plot_data(data_as_dict):
    plot_data = dict()

    for eq in data['features']:
        ms_since_1970 = eq['properties']['time']
        qualifies, year = date_qualifies(ms_since_1970)
        if qualifies:
            if year in plot_data:
                plot_data[year] += 1
            else:
                plot_data[year] = 1
    
    return plot_data

def get_second_plot_data(data_as_dict):
    plot_data2 = dict()
    plot_data = get_plot_data(data_as_dict)
    for eq in data['features']:
        ms_since_1970 = eq['properties']['time']
        qualifies, year = date_qualifies(ms_since_1970)
        if qualifies:
            if year in plot_data2:
                plot_data2[year] += eq['properties']['mag']
            else:
                plot_data2[year] = eq['properties']['mag']

    for key,value in plot_data2.items():
        plot_data2[key] = value / plot_data[key]

    return plot_data2


pd = get_plot_data(data)

plt.plot(pd.keys(), pd.values())
plt.show()

pd2 = get_second_plot_data(data)
plt.plot(pd2.keys(), pd2.values())
plt.show()