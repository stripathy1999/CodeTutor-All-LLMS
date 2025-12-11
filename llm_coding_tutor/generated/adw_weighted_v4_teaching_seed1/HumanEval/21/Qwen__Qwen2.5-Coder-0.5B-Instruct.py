from typing import *
from collections import *

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        raise ValueError("All numbers in the list are the same.", "The list is already unit.")
    
    normalized_values = [(x - min_val) / (max_val - min_val) for x in numbers]
    
    return normalized_values