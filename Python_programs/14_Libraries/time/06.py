# strftime(): Converts a struct_time object to a string based on the specified format.

import time 

local_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted time: ",formatted_time)

"""
    Output:
        Formatted time:  2024-03-07 11:24:47
"""