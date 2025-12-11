def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Initialize the first two Fibonacci numbers
    fib1, fib2 = 0, 1
    
    # Generate Fibonacci numbers until we find the n-th prime
    while True:
        fib_next = fib1 + fib2
        if is_prime(fib_next):
            return fib_next
        
        # Move to the next Fibonacci number
        fib1, fib2 = fib2, fib_next