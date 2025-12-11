def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Create a copy of the array to check for palindrome properties
    reversed_arr = arr[::-1]
    
    # Initialize the change count
    change_count = 0
    
    # Iterate through the array and compare elements with the reversed version
    for i in range(len(arr)):
        # If elements do not match, increment the change count
        if arr[i]!= reversed_arr[i]:
            change_count += 1
    
    return change_count