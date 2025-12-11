from typing import *
from collections import *

def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    
    return c

# Test the function with provided data points
assert fibfib(1) == 0, "Test case 1 failed"
assert fibfib(5) == 4, "Test case 2 failed"
assert fibfib(8) == 24, "Test case 3 failed"
print("All test cases passed successfully.")```