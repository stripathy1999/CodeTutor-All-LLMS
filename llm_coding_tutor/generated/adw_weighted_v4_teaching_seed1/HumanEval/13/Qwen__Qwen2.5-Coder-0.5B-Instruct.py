from typing import *
from collections import *

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    
    # Edge cases: if either number is zero, the GCD is zero
    if a == 0 or b == 0:
        return 0
    
    # Use Euclidean algorithm to find GCD
    while b!= 0:
        a, b = b, a % b
    
    return a

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5