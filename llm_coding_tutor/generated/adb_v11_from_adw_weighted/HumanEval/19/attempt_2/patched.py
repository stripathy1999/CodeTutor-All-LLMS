def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert the input string into a list of integers
    numbers = list(map(int, numbers.split()))
    
    # Sort the list of integers
    numbers.sort()
    
    # Join the sorted list of integers back into a string
    return ''.join(map(str, numbers))