def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over the list with index
    for i in range(1, len(lst), 2):  # Start from index 1 and increment by 2 to only consider odd indices
        if lst[i] % 2 == 0:  # Check if the element is even
            total_sum += lst[i]
    
    return total_sum