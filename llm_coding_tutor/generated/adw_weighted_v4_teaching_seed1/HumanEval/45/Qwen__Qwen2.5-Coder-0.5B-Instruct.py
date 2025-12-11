def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Both sides must be numbers.")
    if a <= 0 or h <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    
    return 0.5 * a * h

# Test cases
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 2))  # Output: 10.0
print(triangle_area(7, 0))   # Output: ValueError