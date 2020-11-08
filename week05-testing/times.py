import datetime
import requests
import json

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    if(start_time_s>=end_time_s):
        raise ValueError('The end of the time range has to come strictly after its start.')
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            # both ranges need to start before the other ends, otherwise there is no overlap!
            if start1 <= end2 and start2 <= end1: 
                low = max(start1, start2)
                high = min(end1, end2)
                if high == low:
                    continue
                overlap_time.append((low, high))
    return overlap_time

def iss_passes(lat, lon, n = 1):
    response = requests.get("http://api.open-notify.org/iss-pass.json",
                        params={
                            'lat': lat,
                            'lon': lon,
                            'n': n
                        })
    if response.status_code != 200:
        # if the request failed for some reason
        return []

    response = response.json()['response']

    time_range = [(datetime.datetime.fromtimestamp(x['risetime']).strftime("%Y-%m-%d %H:%M:%S"), 
                datetime.datetime.fromtimestamp(x['risetime']+x['duration']).strftime("%Y-%m-%d %H:%M:%S"))
                for x in response]
    return time_range

if __name__ == "__main__":

    # large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    # short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    # print(compute_overlap_time(large, short)) 
    print(iss_passes(29.55,95.1,n=5))