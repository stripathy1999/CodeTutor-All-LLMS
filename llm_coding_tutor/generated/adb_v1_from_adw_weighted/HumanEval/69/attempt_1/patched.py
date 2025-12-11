def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Initialize variables to track the maximum value and its frequency
    max_value = -1
    max_frequency = 0
    
    # Iterate through each number in the list
    for num in lst:
        # Check if the number is greater than zero
        if num > 0:
            # Increment the frequency of the number
            num_frequency += 1
            
            # Update the maximum value if the current number is greater
            if num_frequency > max_frequency:
                max_value = num
                max_frequency = num_frequency
    
    # Return the maximum value if found, otherwise return -1
    return max_value if max_value!= -1 else -1