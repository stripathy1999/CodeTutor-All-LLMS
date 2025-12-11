def common(l1: list, l2: list) -> list:
    # Convert lists to sets to remove duplicates and allow for efficient lookups
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets
    common_elements = set1.intersection(set2)
    
    # Return the sorted unique common elements
    return sorted(common_elements)

# Test cases
assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
assert common([5, 3, 2, 8], [3, 2]) == [2, 3]```