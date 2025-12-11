from typing import *
import sys

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start with the largest possible divisor that is less than n
    max_divisor = n // 2
    
    # Try to divide n by each number from max_divisor down to 1
    while max_divisor > 1:
        if n % max_divisor == 0:
            return max_divisor
        max_divisor -= 1
    
    # If no divisor is found, n itself is a divisor
    return n

# Example usage:
print(largest_divisor(15))  # Output: 5