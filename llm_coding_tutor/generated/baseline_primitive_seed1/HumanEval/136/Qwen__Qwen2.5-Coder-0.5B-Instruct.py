def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    # Find the largest negative integer
    largest_negative = max(num for num in lst if num < 0)
    
    # Find the smallest positive integer
    smallest_positive = min(num for num in lst if num > 0)
    
    return (largest_negative, smallest_positive)

# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))              # Output: (None, None)
print(largest_smallest_integers