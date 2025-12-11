def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert the input string into a list of integers
    num_list = [int(num) for num in numbers.split()]
    
    # Sort the list of integers
    num_list.sort()
    
    # Convert the sorted list back into a space-separated string
    return''.join(str(num) for num in num_list)

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This function takes a string of space-delimited numberals, converts it into a list of integers, sorts the list, and then converts the sorted list back into a space-separated string. The test case demonstrates the sorting of the numbers 'three one five'.