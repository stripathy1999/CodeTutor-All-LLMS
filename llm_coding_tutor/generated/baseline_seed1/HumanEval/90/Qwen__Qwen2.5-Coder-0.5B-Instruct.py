from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if not lst:
        return None
    
    # Remove duplicates by converting to a set and back to a list
    unique_lst = list(set(lst))
    
    # Check if there are at least two unique elements
    if len(unique_lst) < 2:
        return None
    
    # Sort the unique list in ascending order
    unique_lst.sort()
    
    # Return the second element in the sorted list
    return unique_lst[1]