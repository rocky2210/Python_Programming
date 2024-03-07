# gmtime(): Returns the current time in UTC as a struct_time object.

import time

utc_time = time.gmtime()
print("UTC time: ",utc_time)

print("\ntm_month:",utc_time.tm_mon)

"""
    Output:
        UTC time:  time.struct_time(tm_year=2024, tm_mon=3, tm_mday=7, tm_hour=5, tm_min=38, tm_sec=58, tm_wday=3, tm_yday=67, tm_isdst=0)    

        tm_month: 3
"""