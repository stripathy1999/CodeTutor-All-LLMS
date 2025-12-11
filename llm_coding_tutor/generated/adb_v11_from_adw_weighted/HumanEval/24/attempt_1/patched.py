def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and move downwards to find the largest divisor
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    # If no divisor is found, return 1 (since 1 is a divisor of any number)
    return 1