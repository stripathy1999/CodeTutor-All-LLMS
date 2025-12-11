from typing import *
from collections import *

def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Initialize sum to 0
    sum_odd = 0
    
    # Iterate over the list with index
    for i in range(len(lst)):
        # Check if the position is even and the number is odd
        if i % 2 == 0 and lst[i] % 2!= 0:
            # Add the odd number to the sum
            sum_odd += lst[i]
    
    # Return the sum
    return sum_odd

# Test cases
assert solution([5, 8, 7, 1]) == 12
assert solution([3, 3, 3, 3, 3]) == 9
assert solution([30, 13, 2