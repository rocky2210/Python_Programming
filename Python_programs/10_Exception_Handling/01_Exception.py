"""
try :
        The code which may 'raise' errors
                                    IO errors ,keyerrors
except:

else:
    this runs when no
finally:
    it will always runs
"""

import sys
try:
    c = a + b
except:
    print("Some error happend",sys.exc_info()[0])