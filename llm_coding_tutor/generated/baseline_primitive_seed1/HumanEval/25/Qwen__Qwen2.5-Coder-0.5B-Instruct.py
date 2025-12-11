from typing import *
from collections import *

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    divisor = 2
    while n >= divisor:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # Should print [2, 2, 2]
print(factorize(25))  # Should print [5, 5]
print(factorize(70))  # Should print [2, 5, 7]Let's break down the problem step-by-step and then write