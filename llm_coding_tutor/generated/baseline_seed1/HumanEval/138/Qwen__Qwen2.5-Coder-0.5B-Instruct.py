```python
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Since the smallest sum of four even numbers is 2 + 2 + 2 + 2 = 8,
    # any number less than 8 cannot be expressed as such a sum.
    if n < 8:
        return False
    
    # If n is even, it can always be expressed as the sum of 4 even numbers.
    return True

# Test cases to verify the correctness of the function
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(10) == True
assert is_equal_to_sum_even(12) == True
assert is_equal_to_sum_even(14) == True
assert is_equal_to_sum_even(16) == True
assert is_equal_to_sum