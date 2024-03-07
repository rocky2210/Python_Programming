# timezone(): Returns the number of seconds west of UTC (negative for locations east of UTC).

import time

timezone_offset = time.timezone
print("Timezone offset:", timezone_offset, "seconds")

"""
    Output:
        Timezone offset: -19800 seconds
"""