from math import factorial

def special_factorial(n):
    return factorial(n) * factorial(n-1) * factorial(n-2) *... * factorial(1)

# Test the function
assert special_factorial(4) == 288, "Test case 1 failed"
assert special_factorial(5) == 34560, "Test case 2 failed"
assert special_factorial(10) == 3628800, "Test case 3 failed"

print("All test cases passed successfully.")```