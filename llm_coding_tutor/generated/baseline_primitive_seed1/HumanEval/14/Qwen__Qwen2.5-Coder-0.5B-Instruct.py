from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(len(string))]

# test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']The given code snippet defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes. The function uses list comprehension to create a new list containing all possible substrings of the input string, starting from the first character and ending at each character in the string.

Here's a breakdown of the code:

1. **Function Definition**: The function `all_prefixes` is defined to take one parameter: `string`, which is expected to be a string.

2. **Return Type**: The function returns a list of strings. This is because the function creates a new list from a list comprehension, which can be used to generate prefixes.

3. **List Comprehension**:
   - The list comprehension `[string[:i] for i in range(len(string))]