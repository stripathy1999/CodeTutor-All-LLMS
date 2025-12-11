```python
from typing import List

def sort_third(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Extract elements at indices divisible by three
    third_elements = [l[i] for i in range(0, len(l), 3)]
    
    # Sort the extracted elements
    third_elements.sort()
    
    # Create a new list to store the result
    result = []
    
    # Place the sorted elements back into their original positions
    for i in range(0, len(l), 3):
        result.append(third_elements[i])
    
    return result