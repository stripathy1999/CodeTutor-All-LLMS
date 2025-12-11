def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Check if n is a prime number
    if n <= 1:
        return y
    elif n <= 3:
        return x
    elif n % 2 == 0 or n % 3 == 0:
        return y
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return y
            i += 6
        return x

# Test cases
print(x_or_y(7, 34, 12))  # Expected output: 34
print(x_or_y(15, 8, 5))  # Expected output: 5