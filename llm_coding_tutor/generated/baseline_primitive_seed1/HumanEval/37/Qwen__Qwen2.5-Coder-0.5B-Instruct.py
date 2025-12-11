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
    # Separate even and odd indices
    even_indices = [i for i in range(len(l)) if l[i] % 2 == 0]
    odd_indices = [i for i in range(len(l)) if l[i] % 2!= 0]

    # Sort even indices
    even_indices.sort()

    # Create a new list to store the result
    result = []
    even_index = 0

    # Fill the result with sorted even indices
    for i in range(len(l)):
        if i in even_indices:
            result.append(l[i])
        else:
            result.append(odd_indices