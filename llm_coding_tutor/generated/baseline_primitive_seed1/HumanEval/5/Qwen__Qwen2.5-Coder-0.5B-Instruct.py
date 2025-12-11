from typing import *
from collections import *

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [numbers[0]] + [delimeter] + [numbers[i+1] for i in range(1, len(numbers)-1)]

# check function to verify correctness
def check_function():
    assert intersperse([], 4) == [], "Test case 1 failed"
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3], "Test case 2 failed"
    assert intersperse([5, 6, 7], 10) == [5, 10, 6, 10, 7], "Test case 3 failed"
    assert intersperse([100], 50) == [100], "Test case 4 failed"