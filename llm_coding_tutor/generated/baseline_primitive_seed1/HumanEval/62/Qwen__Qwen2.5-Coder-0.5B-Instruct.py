from typing import *
from collections import *

def derivative(xs: list) -> List[int]:
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i*x for i,x in enumerate(xs)][1:]
```

This code defines a function `derivative` that takes a list of integers representing the coefficients of a polynomial and returns its derivative as a new list. The function uses list comprehension to iterate over the input list, adding each coefficient to the result list, except for the first element, which is the constant term. The derivative is then returned as a new list.