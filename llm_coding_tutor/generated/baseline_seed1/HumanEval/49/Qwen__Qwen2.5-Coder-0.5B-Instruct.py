def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # Ensure n is within the bounds of p
    if n >= p:
        return 0
    
    result = 1
    base = 2
    
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        
        # Square the base
        base = (base ** 2) % p
        
        # Divide n by 2
        n //= 2
    
    return result