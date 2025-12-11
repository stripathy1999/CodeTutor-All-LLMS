def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Test cases
assert fib(10) == 55, "Test case 1 failed"
assert fib(1) == 1, "Test case 2 failed"
assert fib(8) == 21, "Test case 3 failed"
print("All test cases passed!")<|


```