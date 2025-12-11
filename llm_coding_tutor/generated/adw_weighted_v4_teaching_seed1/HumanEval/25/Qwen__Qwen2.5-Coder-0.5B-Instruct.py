# Import necessary packages
from typing import List

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
    # Start with the smallest prime factor
    factors = [2]
    
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is still greater than 2, then it's a prime number itself
    if n > 2:
        factors.append(n)
    
    return factors