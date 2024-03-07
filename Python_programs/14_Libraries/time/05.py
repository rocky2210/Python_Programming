# localtime(): Returns the current time in local timezone as a struct_time object.

import time

local_time = time.localtime()
print("Local time: ",local_time)

"""
    Output:
        Local time:  time.struct_time(tm_year=2024, tm_mon=3, tm_mday=7, tm_hour=11, tm_min=10, tm_sec=13, tm_wday=3, tm_yday=67, tm_isdst=0)
"""