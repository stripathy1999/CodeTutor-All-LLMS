def is_sorted(lst):
    # Check if the list has more than one duplicate of the same number
    duplicates = Counter(lst)
    if duplicates.values() > 1:
        return False
    
    # Check if the list is sorted
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    
    return True