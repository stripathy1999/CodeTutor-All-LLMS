def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 

    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        # Check for divisibility by 2
        if a % 2 == 0:
            return False
        # Check for divisibility by 3
        if a % 3 == 0:
            return False
        # Check for divisibility by 5
        if a % 5 == 0:
            return False
        # Check for divisibility by 7
        if a % 7 == 0:
            return False
        # Check for divisibility by 11
        if a % 11 == 0:
            return False
        # Check for divisibility by 13
        if a % 13 == 0:
            return False
        # Check for divisibility by 17
        if a % 17 == 0:
            return False
        # Check for divisibility by 19
        if a % 19 == 0:
            return False
        # Check for divisibility by 23
        if a % 23 == 0:
            return False
        # Check for divisibility by 29
        if a % 29 == 0:
            return False
        # Check for divisibility by 31
        if a % 31 == 0:
            return False
        # Check for divisibility by 37
        if a % 37 == 0:
            return False
        # Check for divisibility by 41
        if a % 41 == 0:
            return False
        # Check for divisibility by 43
        if a % 43 == 0:
            return False
        # Check for divisibility by 47
        if a % 47 == 0:
            return False
        # Check for divisibility by 53
        if a % 53 == 0:
            return False
        # Check for divisibility by 59
        if a %