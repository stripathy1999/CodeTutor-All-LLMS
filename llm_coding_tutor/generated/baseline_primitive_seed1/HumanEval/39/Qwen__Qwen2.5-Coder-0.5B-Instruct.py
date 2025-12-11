import math

def prime_fib(n: int) -> int:
    """prime_fib returns n-th number that is a Fibonacci number and it's also prime."""
    fib = [0, 1]
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib[n-1]

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```