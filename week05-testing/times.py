import datetime
import requests
import json

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    if start_time >= end_time:
        raise ValueError("End time should be later than Start time.")

    d = 1.0 * (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1.0 / number_of_intervals - 1.0)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = None
            high = None
            if start1 < start2 < end1:
                low = start2
                high = min(end1, end2)
            elif start2 < start1 < end2:
                low = start1
                high = min(end1, end2)
            if low != None:
                overlap_time.append((low, high))
    return overlap_time

def fetch_iss_passes(lat, lon, n=1):
    params = {}
    params['lat'] = lat
    params['lon'] = lon
    params['n'] = n
    return requests.get("http://api.open-notify.org/iss-pass.json", params=params)

def json_to_passes(data):
    passes = []
    for d in data['response']:
        duration = d['duration']
        risetime = d['risetime']
        passes.append((datetime.datetime.fromtimestamp(risetime),
                       datetime.datetime.fromtimestamp(risetime + duration)))
    return passes

def iss_passes(lat, lon, n=1):
    if lat < -80 or lat > 80 or lat == 0:
        raise ValueError("Latitude must be non-zero and between -80 and 80.")
    if lon < -180 or lon > 180 or lon == 0:
        raise ValueError("Longitude must be non-zero and between -180 and 180")
    if int(n) != n or n < 1:
        raise ValueError("n must be a positive integer.")

    data = json.loads(fetch_iss_passes(lat, lon, n).text)
    passes = json_to_passes(data)
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in passes]

if __name__ == "__main__":
    print(iss_passes(23, 5, 3))