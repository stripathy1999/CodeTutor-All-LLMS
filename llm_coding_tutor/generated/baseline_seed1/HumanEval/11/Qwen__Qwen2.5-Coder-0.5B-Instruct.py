from typing import *
from collections import *

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert strings to lists of integers
    list_a = [int(digit) for digit in a]
    list_b = [int(digit) for digit in b]
    
    # Perform XOR operation
    xor_result = []
    for bit_a, bit_b in zip(list_a, list_b):
        xor_result.append(bit_a ^ bit_b)
    
    # Convert the list of integers back to a string
    return ''.join(map(str, xor_result))