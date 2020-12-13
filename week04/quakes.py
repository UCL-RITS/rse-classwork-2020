"""A script to find the biggest earthquake in an online dataset."""

# At the top of the file, import any libraries you will use.
import requests
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
if __name__ == "__main__":

    class earthq:

        def get_data(self):

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

            with open('quakes.txt', 'w') as textfile:
                textfile.write(quakes.text)

        def load_json(self):
            
            with open('quakes.txt', 'r') as jsonfile:
                self.json_quakes = json.load(jsonfile)
            self.features = self.json_quakes['features']
            
        def findmax(self):

            # the more subtle approach

            largest = self.features[0]
            for i in self.features:
                if i['properties']['mag'] >= largest['properties']['mag']:
                    largest = i
            max_magnitude = largest['properties']['mag']
            coords = largest['geometry']['coordinates']
            print(f"The maximum magnitude is {max_magnitude} and it occured at coordinates {coords}.")

            #my initial longer approach

            # mags=[]
            # places =[]
            # for i in self.features:
            #     mags.append(i['properties']['mag'])
            #     places.append(i['properties']['place'])
            
            # maxmag=[]
            # for j in range(len(mags)):
            #     if mags[j] == max(mags):
            #         maxmag.append([mags[j],places[j]])

        def plots(self):

            years=[]
            for i in self.features:
                years.append(datetime.datetime.fromtimestamp(i['properties']['time']/1000).year)


            years_unique, counts = np.unique(years,return_counts=True)

 
            plt.bar(years_unique, counts)
            plt.xticks(np.arange(min(years), max(years)+1))
            plt.xlabel('Year')
            plt.ylabel('Frequency')
            plt.title('Earthquake frequency per year')
            plt.show()
            plt.clf()


            mags = []
            for i in self.features:
                mags.append(i['properties']['mag'])

            listofmags=[]    
            for j in years_unique:
                mags_per_year=[]
                for i in range(len(self.features)):
                    if years[i] == j:
                        mags_per_year.append(mags[i])
                listofmags.append(mags_per_year)
            avg_mag = [np.mean(i) for i in listofmags]
            
            plt.bar(years_unique, avg_mag)
            plt.xticks(np.arange(min(years), max(years)+1))
            plt.xlabel('Year')
            plt.ylabel('Average Magnitude')
            plt.title('Earthquake average magnitude per year')
            
            plt.show()


EQ = earthq()
EQ.get_data()
EQ.load_json()
EQ.findmax()
EQ.plots()