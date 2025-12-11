from typing import *
from collections import *

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list
    sorted_l = sorted(l)
    
    # Calculate the median
    n = len(sorted_l)
    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_l[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2.0