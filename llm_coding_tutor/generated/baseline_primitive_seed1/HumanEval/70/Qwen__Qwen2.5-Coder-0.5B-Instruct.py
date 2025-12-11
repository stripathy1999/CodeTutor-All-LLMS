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
    # Sort the list
    lst.sort()
    
    # Initialize pointers for the smallest and largest elements
    left = 0
    right = len(lst) - 1
    
    # Create a new list to store the result
    result = []
    
    # Iterate through the sorted list
    while left <= right:
        if left == right:
            # If there's only one element left, add it to the result
            result.append(lst[left])
        else:
            # Add the smallest element
            result.append(lst[left])
            # Add the largest element
            result.append(lst[right])
        
        # Move the pointers towards the center
        left +=