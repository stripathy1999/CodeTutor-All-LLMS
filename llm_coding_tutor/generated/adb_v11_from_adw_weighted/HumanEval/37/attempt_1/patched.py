def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Sort the even indices of the list
    even_indices = sorted(range(len(l)), key=lambda i: l[i])
    
    # Create a new list to store the result
    result = []
    
    # Iterate over the original list
    for i in range(len(l)):
        if i % 2 == 0:
            # Use the sorted even index to get the value from the sorted list
            result.append(even_indices[i // 2])
        else:
            # Use the original value
            result.append(l[i])
    
    return result