import math

def prime_fib(n: int):
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    fib = 0
    count = 0
    
    while fib < n:
        fib += 1
        if is_prime(fib):
            count += 1
    
    return fib