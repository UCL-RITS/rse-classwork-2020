#passes.py
def iss_passes(lat = 51.482218, lon = -.264547, alt =10, n=5):
    import requests
    import json
    import datetime

    response = requests.get("http://api.open-notify.org/iss-pass.json",
                                    params={
                                        "lat": lat,
                                        "lon": lon,
                                        "alt": alt,
                                        "n": n})

    
    passes=response.json()['response']

    print(response)

#    for items in passes:
#        print 

#    return [(datetime.datetime.fromtimestamp(item['risetime']).strftime("%Y-%m-%d %H:%M:%S"),
#             (datetime.datetime.fromtimestamp(item['risetime'] + item['duration'])).strftime("%Y-%m-%d %H:%M:%S"))
#            for item in passes]
