# get_clock_info(): Returns information about the specified clock.

import time

clock_info = time.get_clock_info('time')
print("Clock info:", clock_info)

"""
    Output:
        Clock info: namespace(implementation='clock_gettime(CLOCK_REALTIME)', monotonic=False, adjustable=True, resolution=1e-09)
"""