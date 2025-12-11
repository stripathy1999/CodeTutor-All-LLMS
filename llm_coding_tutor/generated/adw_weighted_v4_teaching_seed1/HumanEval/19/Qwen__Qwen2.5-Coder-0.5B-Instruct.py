from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert the input string into a list of integers
    num_list = list(map(int, numbers.split()))
    
    # Sort the list of numbers
    num_list.sort()
    
    # Join the sorted list back into a string
    sorted_string =''.join(map(str, num_list))
    
    return sorted_string
# NOTE: Rubric corruption applied, dropped 3 hints
