"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
# import ...

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...

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

    d = json.loads(quakes.text)
    places = {i['properties']['place']:i['properties']['mag'] for i in d['features']}
    s = max(places,key = places.get)

    coords = [i['geometry']['coordinates'] for i in d['features'] if i['properties']['place'] == s][0]
    
    max_magnitude = places[s]

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at coordinates {coords}.")
