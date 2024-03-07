# process_time(): Returns the sum of the system and user CPU time of the current process in seconds.

import time

start_time = time.process_time()
# Code to measure CPU time
end_time = time.process_time()
cpu_time = end_time - start_time
print("CPU time:", cpu_time, "seconds")

"""
    Output:
        CPU time: 2.599999999998437e-06 seconds
"""