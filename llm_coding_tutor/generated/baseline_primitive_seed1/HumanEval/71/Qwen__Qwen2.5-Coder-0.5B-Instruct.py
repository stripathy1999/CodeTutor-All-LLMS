def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if a + b > c and a + c > b and b + c > a:
        area = (a * b * c) / 2
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # Expected output: 6.00
print(triangle_area(1, 2, 10))   # Expected output: -1
```

This function checks if the given sides can form a valid triangle and then calculates the area if they do. If not, it returns -1. The result is rounded to two decimal places