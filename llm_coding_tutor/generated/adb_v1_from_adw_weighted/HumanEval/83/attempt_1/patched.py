def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 18
    else:
        # For n > 2, calculate the count
        count = 18 * (10**(n-2))
        # Add the count for numbers starting with 1
        count += 18 * (10**(n-3))
        return count