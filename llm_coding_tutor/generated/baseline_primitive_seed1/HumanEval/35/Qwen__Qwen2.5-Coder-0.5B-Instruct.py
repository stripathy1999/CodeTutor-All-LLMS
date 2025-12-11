from typing import *
from collections import *

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Check function to verify the correctness of the solution
def check_solution():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    print("All tests passed.")

check_solution()
```

This code snippet defines a function `max_element` that takes a list as input and returns the maximum element in the list. It uses Python's built-in `max` function, which is efficient and concise. The `check_solution` function is used to verify the correctness of `max_element` with provided data points.