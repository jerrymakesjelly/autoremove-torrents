import sys

# This variable 'inf_' represents infinity
inf_ = None

if sys.version_info >= (3, 5, 0):
    import math
    inf_ = math.inf
else:
    inf_ = float('inf')
