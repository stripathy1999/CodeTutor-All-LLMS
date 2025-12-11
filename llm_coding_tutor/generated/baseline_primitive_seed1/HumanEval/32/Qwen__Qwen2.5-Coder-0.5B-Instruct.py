from typing import *
from collections import *

def poly(xs: List[int], x: float) -> int:
    return sum(coef * pow(x, i) for i, coef in enumerate(xs))

def find_zero(xs: List[int]) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2!= 0:
        raise ValueError("The length of the list must be even.")
    
    return find_zero(xs, 0)

#