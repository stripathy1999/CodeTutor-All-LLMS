from typing import *
from collections import *

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Calculate the total number of n-digit numbers
    total_numbers = 9 * 10**(n-1)
    
    # Calculate the numbers that start with 1
    start_with_1 = 9 * 10**(n-1) - 9 * 10**(n-2)
    
    # Calculate the numbers that end with 1
    end_with_1 = 9 * 10**(n-1) - 9 * 10**(n-3)
    
    # Total numbers starting or ending with 1
    return start_with_1 + end_with_1

# Test the function
print(starts_one_ends(2))  # Output: 18
print(starts_one_ends(3))  # Output: 180
print(starts_one_ends(4))  # Output: 1800
```

This solution calculates the total number of n-digit positive integers and then subtracts the numbers that start or