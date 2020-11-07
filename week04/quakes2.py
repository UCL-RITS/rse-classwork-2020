{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "quakes = requests.get(\"http://earthquake.usgs.gov/fdsnws/event/1/query.geojson\",\n",
    "                      params={\n",
    "                          'starttime': \"2000-01-01\",\n",
    "                          \"maxlatitude\": \"58.723\",\n",
    "                          \"minlatitude\": \"50.008\",\n",
    "                          \"maxlongitude\": \"1.67\",\n",
    "                          \"minlongitude\": \"-9.756\",\n",
    "                          \"minmagnitude\": \"1\",\n",
    "                          \"endtime\": \"2018-10-11\",\n",
    "                          \"orderby\": \"time-asc\"}\n",
    "                      )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "requests_json = json.loads(quakes.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(requests_json)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['type', 'metadata', 'features', 'bbox'])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests_json.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(requests_json['features'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['type', 'properties', 'geometry', 'id'])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests_json['features'][0].keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['mag', 'place', 'time', 'updated', 'tz', 'url', 'detail', 'felt', 'cdi', 'mmi', 'alert', 'status', 'tsunami', 'sig', 'net', 'code', 'ids', 'sources', 'types', 'nst', 'dmin', 'rms', 'gap', 'magType', 'type', 'title'])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests_json['features'][0]['properties'].keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.6"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests_json['features'][0]['properties']['mag']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'type': 'Point', 'coordinates': [-2.81, 54.77, 14]}"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests_json['features'][0]['geometry']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "quakes=requests_json['features']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.8"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "largest_so_far=quakes[0]\n",
    "for quake in quakes:\n",
    "    if quake['properties']['mag']>largest_so_far['properties']['mag']:\n",
    "        largest_so_far=quake\n",
    "largest_so_far['properties']['mag']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Latitude: 52.52 Longitude: -2.15\n"
     ]
    }
   ],
   "source": [
    "lat = largest_so_far['geometry']['coordinates'][1]\n",
    "long = largest_so_far['geometry']['coordinates'][0]\n",
    "print(\"Latitude: {} Longitude: {}\".format(lat, long))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "\n",
    "def request_map_at(lat, long, satellite=True,\n",
    "                   zoom=10, size=(400, 400)):\n",
    "    base = \"https://static-maps.yandex.ru/1.x/?\"\n",
    "\n",
    "    params = dict(\n",
    "        z=zoom,\n",
    "        size=\"{},{}\".format(size[0], size[1]),\n",
    "        ll=\"{},{}\".format(long, lat),\n",
    "        l=\"sat\" if satellite else \"map\",\n",
    "        lang=\"en_US\"\n",
    "    )\n",
    "\n",
    "    return requests.get(base, params=params)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "map_png = request_map_at(lat, long, zoom=10, satellite=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from IPython.display import Image\n",
    "Image(map_png.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
