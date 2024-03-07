# strptime(): Parses a string representing a time according to the specified format.

import time

time_string = "2024-03-07 15:30:00"
parsed_time = time.strptime(time_string,"%Y-%m-%d %H:%M:%S")
print("Parsed time: ",parsed_time)

"""
    Output:
        Parsed time:  time.struct_time(tm_year=2024, tm_mon=3, tm_mday=7, tm_hour=15, tm_min=30, tm_sec=0, tm_wday=3, tm_yday=67, tm_isdst=-1)
"""