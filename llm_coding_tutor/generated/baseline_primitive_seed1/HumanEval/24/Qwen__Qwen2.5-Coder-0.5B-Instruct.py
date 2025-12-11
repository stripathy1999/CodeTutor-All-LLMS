def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for divisor in range(n-1, 0, -1):
        if n % divisor == 0:
            return divisor

# test the function with a check
assert largest_divisor(15) == 5, "Test case 1 failed"
assert largest_divisor(28) == 14, "Test case 2 failed"
assert largest_divisor(77) == 7, "Test case 3 failed"
print("All test cases passed!")<|endanswer|}