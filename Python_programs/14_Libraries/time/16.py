# daylight(): Returns True if the local timezone should observe daylight saving time, False otherwise.

import time

is_daylight = time.daylight
print("Daylight saving time observed:", is_daylight)

"""
    Output:
        Daylight saving time observed: 0
"""