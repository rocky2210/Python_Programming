# ctime(): Converts a time in seconds since the epoch to a string representing local time.

import time

current_time = time.time()
print("Current time",time.ctime(current_time))

"""
    Output:
        Current time Thu Mar  7 10:55:34 2024
"""