# import ...

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
from datetime import datetime
import json
import requests
import matplotlib.pyplot as plt
from PIL import Image

def get_quake_data_from_URL():
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
    #print(quakes.text[0:100])

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    #print(f"The maximum magnitude is {max_magnitude} "
    #      f"and it occured at coordinates {coords}.")

    with open('quakes.json', 'w') as quakes_js:
        quakes_js.write(quakes.text)

    with open('quakes.json', 'r') as target:
        myfile_str = target.read()

    myfile = json.loads(myfile_str)

    return myfile

def get_max_mag_quake_detail(json_file):

    quake_detail =[]
    features = [dict(feature) for feature in myfile['features']]

    for i in range(len(features)):
        if 'United Kingdom' in features[i]['properties']['place']:
            x = features[i]['properties']['time']
            d = datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d')
            quake_detail.append([features[i]['properties']['mag'],d,features[i]['properties']['place'],features[i]['geometry']['coordinates'] ])
    
       
    #max_magnitude = [quake_detail[i] for i in range(len(quake_detail))  ]
    
    #max_mag = max_magnitude[0][0]
    #dates = [each_quake[1] for each_quake in max_magnitude]
    #places = [each_quake[2] for each_quake in max_magnitude]
    #coords = [each_quake[3] for each_quake in max_magnitude]

    return quake_detail


def request_map_at(lat, long, satellite=False,
                   zoom=10, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"
  
    params = dict(
        z = zoom,
        size = str(size[0]) + "," + str(size[1]),
        ll = str(long) + "," + str(lat),
        l = "sat" if satellite else "map",
        lang = "en_US"
    )

    return requests.get(base,params=params)

if __name__ == "__main__":
    # ...do things here to find the results...
    myfile = get_quake_data_from_URL()
    details_of_quakes = get_max_mag_quake_detail(myfile)

    #print(f"The maximum magnitude is {max_mag} "
    #    f"and it occured at coordinates {coords}.")
    # 
    #map_response = request_map_at(coords[0][1],coords[0][0])
    #print(map_response.url)
    #im = Image.open(requests.get(map_response.url, stream=True).raw)
    #plt.imshow(im)
    #plt.show()

    magnitude = [details_of_quakes[i][0] for i in range(len(details_of_quakes))]
    dates = [details_of_quakes[i][1][0:4] for i in range(len(details_of_quakes))]
    
    nBins = len(set(dates))
    #print(nBins)
    plt.figure(figsize = (10,5))    
    plt.title('Frequency of Quakes per Year')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.hist(dates, bins=nBins )
        #graph, graph_axes = plt.subplots()
    #plt.plot(dates, magnitude)
    #plt.setp(graph_axes.get_xticklabels(), visible=False)
    plt.show()
