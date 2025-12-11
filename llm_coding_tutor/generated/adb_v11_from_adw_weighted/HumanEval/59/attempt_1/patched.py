def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start checking from the smallest prime number, which is 2
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    # If no factors were found, n itself is prime
    return n