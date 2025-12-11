from typing import *
from collections import *

def sorted_list_sum(lst):
    """Sorts the given list of strings by their lengths and alphabetically.
    Removes strings with odd lengths from the list, ensuring a sorted list.
    Strings with even lengths maintain their original order.
    
    Parameters:
    lst (List[str]): The list of strings to process.
    
    Returns:
    List[str]: A new list containing only the strings with even lengths.
    """
    # Filter out strings with odd lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the filtered strings by length, then alphabetically
    sorted_even_length_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    return sorted_even_length_strings

# Example usage:
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]