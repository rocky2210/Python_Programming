# perf_counter(): Returns a high-resolution performance counter for benchmarking purposes.

import time

start_time = time.perf_counter()
# Code to benchmark
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")

"""
    Output:
        Elapsed time: 1.823000275180675e-06 seconds
"""