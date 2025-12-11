from typing import *
from collections import *

def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd_digit = False
    for digit in str(n):
        if int(digit) % 2!= 0:
            product *= int(digit)
            has_odd_digit = True
    return product if has_odd_digit else 0

# Test cases to verify the correctness of the function
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(111) == 1
assert digits(13579) == 0
assert digits(24680) == 0
assert digits(135790) == 0
assert digits(222222) == 0
assert digits(1111111) == 1
assert