from typing import *
from collections import *

def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # Dictionary to hold the balance between open and close brackets
    balance = {')': 1, '(': -1}
    
    # Iterate through each character in the brackets string
    for char in brackets:
        if char in balance:
            # Increment the balance if it's an opening bracket
            balance[char] += 1
        elif char in balance.values():
            # Decrement the balance if it's a closing bracket
            balance[char] -= 1
            
            # If the balance goes negative, it means there's a closing bracket without a matching opening bracket
            if balance[char] < 0:
                return False
    
    # If all brackets have matching opening and closing pairs, return True
    return True