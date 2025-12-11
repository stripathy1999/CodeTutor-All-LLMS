import math

def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return True if the three
    sides form a right-angled triangle, False otherwise.
    
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    # Sort the sides to ensure the largest side is considered as the hypotenuse
    sides = sorted([a, b, c])
    
    # Check if the Pythagorean theorem holds for the sorted sides
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# Test cases
print(right_angle_triangle(3, 4, 5))  # Expected: True
print(right_angle_triangle(1, 2, 3))  # Expected: False
print(right_angle_triangle(5, 12, 13))  # Expected: True
print(right_angle_triangle(10, 6, 8))  # Expected: True
print(right_angle_triangle(7, 24, 25))  # Expected: False