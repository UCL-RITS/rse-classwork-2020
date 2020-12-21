"""Exercise #61 - Code"""

import datetime
import requests

#function to convert the time range into strings of start ta and end tb
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


#function to compute the overlap time
def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
           
            # both ranges need to start before the other ends, otherwise there is no overlap!
            if start1<= end2 and start2 <= end1: 
                low = max(start1, start2)
                high = min(end1, end2)

                # in case they touch exactly (end of one is start of the other) --> no overlap
                if high == low:
                    continue    # jumps to the next iteration of the loop

                overlap_time.append((low, high))

            #note: when there is no overlap, overlap_time = [] stays
    return overlap_time

# Mocking the ISS times from: http://open-notify.org/Open-Notify-API/ISS-Pass-Times/
def iss_passes(lat, lon, n=5):
    """
    Returns a time_range-like output for intervals of time when the International Space Station
    passes at a given location and for a number of days from today.
    """
    iss_request = requests.get("http://api.open-notify.org/iss-pass.json",
                               params={
                                   "lat": lat,
                                   "lon": lon,
                                   "n": n})

    if iss_request.status_code != 200:
        # if the request failed for some reason
        return []
    response = iss_request.json()['response']
    #To convert unix time stamps use datetime.datetime.fromtimestamp function
    return [(datetime.datetime.fromtimestamp(x['risetime']).strftime("%Y-%m-%d %H:%M:%S"),
             (datetime.datetime.fromtimestamp(x['risetime'] + x['duration'])).strftime("%Y-%m-%d %H:%M:%S"))
            for x in response]

# this only runs if this module is run directly, if it is imported somewhere then __name__ == times instead!!
if __name__ == "__main__":
    #converts the time ranges into strings
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(f"large: {large}")
        #[('2010-01-12 10:00:00', '2010-01-12 12:00:00')]
    print(f"short: {short}")
        #[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    # the outputted resulting overlap time 
    overlap_t = compute_overlap_time(large, short)
    print(f"The resulting overlaps are {overlap_t}.")
        #[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    # ISS passes over London
    print("The ISS passes over London:", iss_passes(51.5074, -0.1278))