# mktime(): Converts a struct_time object or a tuple representing a time to seconds since the epoch.

import time

time_tuple = (2024, 3, 7, 12, 30, 0, 0, 0, 0)  # (year, month, day, hour, minute, second, weekday, Julian day, DST)
epoch_time = time.mktime(time_tuple)
print("Seconds since epoch:", epoch_time)

"""
    Output:
        Seconds since epoch: 1709794800.0
"""