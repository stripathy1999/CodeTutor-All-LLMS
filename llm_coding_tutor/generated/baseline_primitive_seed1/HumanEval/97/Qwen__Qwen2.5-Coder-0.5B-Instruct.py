import math

def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    return math.prod([int(x) for x in str(abs(a) * abs(b))]) if a!= 0 else 0
```

This function calculates the product of the unit digits of two integers by taking the absolute values to handle negative numbers and then converting each digit back to an integer. It uses the `math.prod` function to multiply all the digits together. The function handles edge cases where the input is zero or negative by returning 0.