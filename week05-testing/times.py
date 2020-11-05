import datetime


# gives the time range between start time and end time [t1, t2] and [t3,t3]
# d is the time difference
# sec_range gives the difference interval in seconds 
# number of intervals [t2,t3]
def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0): # gaps in seconds - possible in the interval(s)

    if end_time < start_time:
        raise ValueError('End_time is before start_time')

    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") # from date string to datetime objects 
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") # from date string to datetime objects
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1) 
    print('d')
    print(d)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    print(sec_range)

    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range] 
    # from object datetime to string - output: 7200sec 

# gives the overlap time between range 1 [1,t2] and range 2 [t3,t4]
def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            # if start2 < end1 or start1 < end2:
            low = max(start1, start2)
            high = min(end1, end2)
            if low < high:
                overlap_time.append((low, high))
    return overlap_time


if __name__ == "__main__":
    large = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00") # range 1 [t1,t2]
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60) # range 2 [t3,t6] -> [t3,t4][t5,t6]
    # print(large)
    # print(short)
    # print(compute_overlap_time(large, short))