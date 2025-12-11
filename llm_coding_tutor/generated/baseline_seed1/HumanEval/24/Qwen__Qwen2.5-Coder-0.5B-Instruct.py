def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and move downwards to find the largest divisor
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisor is found, return 1 (since 1 is a divisor of every number)

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(28) == 14
assert largest_divisor(13) == 1
assert largest_divisor(1) == 1
assert largest_divisor(0) == 1