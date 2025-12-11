from math import sqrt

def is_prime(num):
    """Check if a number is prime."""
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

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes

# test the function
print(count_up_to(5))  # Output: [2, 3]
print(count_up_to(11)) # Output: [2, 3, 5, 7]
print(count_up_to(0))  # Output: []
print(count_up_to(20)) # Output: [2, 3, 5,