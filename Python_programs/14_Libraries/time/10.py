# monotonic(): Returns a clock with the highest available resolution to measure a short duration.

import time

start_time = time.monotonic()
# measure time
end_time = time.monotonic()
elapsed_time = end_time - start_time
print("Elapsed time: ",elapsed_time,"seconds")

"""
    Output:
        Elapsed time:  1.9756000256165862e-05 seconds
"""