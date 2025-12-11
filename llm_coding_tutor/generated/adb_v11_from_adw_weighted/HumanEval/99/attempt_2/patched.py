def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Convert the string to a float
    num = float(value)
    
    # Check if the number is an integer
    if num.is_integer():
        # Return the integer itself
        return int(num)
    
    # Calculate the absolute difference between the number and its nearest neighbor
    diff = abs(num - round(num))
    
    # Determine the closest integer based on the absolute difference
    if diff < 0.5:
        return round(num)
    else:
        return round(num) + 1