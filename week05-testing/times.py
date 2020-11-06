import datetime

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    if start_time_s > end_time_s: 
        raise ValueError("Start time is later than end time")

    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]

def compute_overlap_helper(tuple1, tuple2):
    start1, end1 = tuple1
    start2, end2 = tuple2
    if(start1 >= end2 or start2 >= end1):
        return tuple()
    else:
        low = max(start1, start2)
        high = min(end1, end2)
        return((low, high))

def compute_overlap_time(range1, range2):
    overlap_time = []
    for tuple1 in range1:
        for tuple2 in range2:
            if(overlap := compute_overlap_helper(tuple1, tuple2)):
                overlap_time.append((overlap))
    return(overlap_time)