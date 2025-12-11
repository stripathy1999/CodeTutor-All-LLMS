def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case: numbers less than 2 have no leading or trailing 1
    if n < 2:
        return 0
    
    # Count numbers starting with 1
    start_with_1 = 9 * (10**(n-1))
    
    # Count numbers ending with 1
    end_with_1 = 9 * (10**(n-1))
    
    # Total numbers that start or end with 1
    total_start_end_with_1 = start_with_1 + end_with_1
    
    # Numbers that both start and end with 1
    start_and_end_with_1 = 8 * (10