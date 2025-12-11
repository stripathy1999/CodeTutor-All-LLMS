def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 2 == 0

# check function to verify the correctness of the solution
def check_solution():
    test_cases = [4, 6, 8, 10, 12]
    expected_results = [False, False, True, True, True]
    for n, expected in zip(test_cases, expected_results):
        result = is_equal_to_sum_even(n)
        assert result == expected, f"Failed on {n}: expected {expected}, got {result}"
    print("All tests passed!")

check_solution()
```

This code defines a function `is_equal_to_sum_even` that checks if a given number `n` can be expressed as the sum of exactly 4 positive even numbers. It also includes a `check_solution` function to verify the correctness of the solution with various test cases.