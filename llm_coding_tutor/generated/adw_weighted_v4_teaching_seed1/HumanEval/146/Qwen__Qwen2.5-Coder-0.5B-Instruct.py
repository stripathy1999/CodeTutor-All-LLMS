from typing import *
import re

def specialFilter(nums: List[int]) -> int:
    """
    Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).

    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    def is_odd_digit(digit: int) -> bool:
        return digit in [1, 3, 5, 7, 9]

    def is_first_last_digit_odd(num: int) -> bool:
        num_str = str(abs(num))
        return is_odd_digit(int(num_str[0])) and is_odd_digit(int(num_str[-1]))

    count = sum(1 for num in nums if num > 10 and is_first_last_digit_odd(num))

    return count

# Example usage:
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2