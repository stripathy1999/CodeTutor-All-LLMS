def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Ensure x and y are positive integers
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be positive integers.")
    
    # Ensure x is less than or equal to y
    if x > y:
        raise ValueError("x must be less than or equal to y.")
    
    # Check if x is even and y is odd, otherwise return -1
    if x % 2 == 0 and y % 2!= 0:
        return y
    elif x % 2!= 0 and y % 2 == 0:
        return x
    
    # Find the maximum even number in the range [x, y]
    return max([x, y])