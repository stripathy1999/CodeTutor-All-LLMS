from typing import List

def sort_even(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Extract elements at even indices
    even_elements = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the extracted elements
    even_elements.sort()
    
    # Create a new list to store the result
    result = []
    
    # Place the sorted even elements back into their original positions
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_elements[even_index])
            even_index += 1
    
    return result