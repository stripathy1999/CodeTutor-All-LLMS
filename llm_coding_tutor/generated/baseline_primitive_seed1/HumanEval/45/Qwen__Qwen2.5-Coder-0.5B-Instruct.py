def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
assert triangle_area(5, 3) == 7.5
```

This solution mirrors the functionality of the original Rust code snippet while using Python's syntax and idioms. The function `triangle_area` calculates the area of a triangle given its length and height. The test case verifies the correctness of the implemented function.