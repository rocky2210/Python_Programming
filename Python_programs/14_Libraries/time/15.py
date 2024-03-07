# altzone(): Returns the offset of the local DST timezone, in seconds west of UTC.

import time

dst_offset = time.altzone
print("DST offset:", dst_offset, "seconds")

"""
    Output:
        DST offset: -19800 seconds
"""