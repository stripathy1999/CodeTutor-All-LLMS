def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # Sort the list in ascending order
    lst.sort()
    
    # Initialize two pointers: one for the smallest number and another for the largest
    left = 0
    right = len(lst) - 1
    
    # Create an empty list to store the result
    result = []
    
    # Alternate between the smallest and largest remaining numbers
    while left <= right:
        # Add the smallest remaining number to the result
        result.append(lst[left])
        left += 1
        
        # If we are still within the bounds, add the largest remaining number
        if left <= right:
            result.append(lst[right])
            right -= 1
    
    return result