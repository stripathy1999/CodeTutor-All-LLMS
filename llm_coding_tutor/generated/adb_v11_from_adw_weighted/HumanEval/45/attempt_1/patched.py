import math

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the semi-perimeter
    s = (a + h) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - h))
    
    return area