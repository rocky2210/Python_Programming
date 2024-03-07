# asctime(): Converts a struct_time object to a string representing a date and time.

import time

local_time = time.localtime()
formatted_time = time.asctime(local_time)
print("Formatted time: ",formatted_time)

"""
    Output:
        Formatted time:  Thu Mar  7 11:35:28 2024
"""