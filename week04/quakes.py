"""A script to find the biggest earthquake in an online dataset."""

import requests
import json
from datetime import date, datetime


class EarthquakeQueryBuilder:
    def __init__(self, **default_args):
        self.query = dict()
        self.query['minmagnitude'] = default_args['min_magnitude']
        self.query['orderby'] = default_args['order_by']

    def earthquakes_in_this_century(self):
        today = date.today().strftime("%Y-%m-%d")
        self.query.update({
            'starttime': "2001-01-01",
            "endtime": today,
        })
        return self

    def earthquakes_in_the_uk(self):
        self.query.update({
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
        })
        return self

    def get_query(self):
        return self.query


# def greeting(name: str) -> str:
#     return 'Hello ' + name


class EarthquakesDataFetcher:
    def __init__(self, queryBuilder: EarthquakeQueryBuilder):
        self.params = queryBuilder.get_query()

    def fetch(self) -> str:
        return requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson", params=self.params).text


queryBuilder = EarthquakeQueryBuilder(
    min_magnitude="1", order_by="time-asc").earthquakes_in_the_uk().earthquakes_in_this_century()

data = EarthquakesDataFetcher(queryBuilder).fetch()

with open('earthquakes.json', 'w') as json_file:
    json.dump(json.loads(data), json_file, indent=2)

with open('earthquakes.json', 'r') as json_file:
    data_string = json_file.read()

data = json.loads(data_string)

max_magnitude = max(feature['properties']['mag']
                    for feature in data['features'])

biggest_earthquakes = [(feature['geometry']['coordinates'], datetime.fromtimestamp(feature['properties']['time'] / 1000).strftime('%Y-%m-%d'))
                       for feature in data['features']
                       if feature['properties']['mag'] == max_magnitude]


print(f"The maximum magnitude is {max_magnitude} "
      f"and it occured at coordinates {[e[0] for e in biggest_earthquakes]}."
      f"They happened on {[e[1] for e in biggest_earthquakes]}")
