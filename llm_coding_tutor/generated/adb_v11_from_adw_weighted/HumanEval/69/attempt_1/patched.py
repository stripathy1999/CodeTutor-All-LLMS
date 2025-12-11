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
    # Create a dictionary to count occurrences of each number
    freq_dict = {}
    for num in lst:
        if num > 0:
            freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Initialize variables to track the result
    result = -1
    max_freq = 0
    
    # Iterate over the dictionary to find the greatest number meeting the criteria
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            if num > result or (num == result and freq > max_freq):
                result = num
                max_freq = freq
    
    return result