# tzname(): Returns a tuple containing the time zone names corresponding to standard and daylight saving time.

import time

timezone_names = time.tzname
print("Timezone names:", timezone_names)

"""
    Output:
        Timezone names: ('IST', 'IST')
"""