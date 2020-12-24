def format_time(dt):
    """
    Converts a time from seconds into a human readable format.

    Adapted function from cpython's Lib/timeit.py
    """
    units = {"nsec": 1e-9, "μsec": 1e-6, "msec": 1e-3, "sec": 1.0}
    unit = None
    precision = 3

    scales = [(scale, unit) for unit, scale in units.items()]
    scales.sort(reverse=True)
    for scale, unit in scales:
        if dt >= scale:
            break

    return f"{dt/scale:.{precision}g} {unit}"
