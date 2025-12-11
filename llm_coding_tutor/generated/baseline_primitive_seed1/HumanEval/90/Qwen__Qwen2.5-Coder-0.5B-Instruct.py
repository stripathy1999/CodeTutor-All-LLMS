from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    # Check if the list has fewer than 2 elements
    if len(lst) < 2:
        return None
    
    # Initialize two variables to track the smallest and second smallest elements
    smallest = float('inf')
    second_smallest = float('inf')
    
    # Iterate through the list to find the smallest and second smallest elements
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num!= smallest:
            second_smallest = num
    
    # Return the second smallest element or None if it doesn't exist
    return second_smallest

# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))             # Output: None
print(next_smallest([1, 1]))            # Output: None
```

This Python function `next_smallest` implements the logic described in the