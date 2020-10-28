"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests 
import json

#Obtain text from web results 
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

print(quakes.text[0:100])
print(type(quakes.text))

#1. Save data in text file to understand a bit more about it
with open('quakes.txt', 'w') as quakes_txt:
    quakes_txt.write(quakes.text)

#2. Parse the data as JSON 
requests_json = json.loads(quakes.text)
print(type(requests_json)) #Prints type of requests_json as dictionary 
print(requests_json.keys()) #Prints out the keys in this large dictionary 

#Obtain just the features from json file 
features = requests_json['features']
print("Type of features:", type(features))

#3. Understand how data is structured into dictionaries and lists:
#Loop through one feature
print(type(features[0])) #Each item in the list is a separate dictionary 
print(features[0].keys())
print(features[0]['properties'])
print(features[0]['properties']['mag'])

#Loop through every item in the list, obtain the magnitude and location of strongest earthquake
mag = [] #Magnitude vector
place = [] #Place vector 

for earthquake in features:
    mag.append(earthquake['properties']['mag'])
    place.append(earthquake['properties']['place'])

#Finding maximum magnitude 
max_magnitude= max(mag)
index = mag.index(max_magnitude)
#print(mag.index(max_magnitude)) #Prints out index of maximum value in this list 

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":
    # ...do things here to find the results...

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
    print(f"The maximum magnitude is {max_magnitude} "
          f"and it occured at place {place[index]}.")
    pass