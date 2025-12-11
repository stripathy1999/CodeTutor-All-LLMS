import math

def right_angle_triangle(a, b, c):
    return math.isclose(a**2 + b**2, c**2)

# Test the function with provided data points
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
```