# Using clock ID constants


import time

# Get information about CLOCK_MONOTONIC clock
monotonic_clock_info = time.get_clock_info('monotonic')
print("CLOCK_MONOTONIC info:", monotonic_clock_info)

# Get information about CLOCK_MONOTONIC_RAW clock
monotonic_raw_clock_info = time.get_clock_info('monotonic_raw')
print("CLOCK_MONOTONIC_RAW info:", monotonic_raw_clock_info)

# Get information about CLOCK_REALTIME clock
realtime_clock_info = time.get_clock_info('realtime')
print("CLOCK_REALTIME info:", realtime_clock_info)

# Get information about CLOCK_PROCESS_CPUTIME_ID clock
process_cputime_clock_info = time.get_clock_info('process_cputime_id')
print("CLOCK_PROCESS_CPUTIME_ID info:", process_cputime_clock_info)

# Get information about CLOCK_THREAD_CPUTIME_ID clock
thread_cputime_clock_info = time.get_clock_info('thread_cputime_id')
print("CLOCK_THREAD_CPUTIME_ID info:", thread_cputime_clock_info)


# Most of them not supported 