def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    if n == 2:
        return 18
    
    # Calculate the number of n-digit numbers that start with 1
    start_with_1 = 9 * (10**(n-1))
    
    # Calculate the number of n-digit numbers that end with 1
    end_with_1 = 9 * (10**(n-1))
    
    # Calculate the number of n-digit numbers that both start and end with 1
    start_and_end_with_1 = 9 * (10**(n-2))
    
    # Total count
    total_count = start_with_1 + end_with_1 - start_and_end_with_1
    
    return total_count