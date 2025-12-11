from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    return sorted(nums, key=lambda x: sum(int(digit) for digit in str(x)))

# check function with provided data points
def check():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11], "Test case 1 failed"
    assert order_by_points([]) == [], "Test case 2 failed"
    assert order_by_points([42, 43, 45, 56]) == [42, 43, 45