from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all spaces from the input string
    cleaned_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Iterate over each character in the cleaned string
    for char in cleaned_string:
        if char == '(':
            # If the current character is an opening parenthesis, add it to the list
            separated_groups.append(char)
        elif char == ')':
            # If the current character is a closing parenthesis, remove the last element from the list
            if separated_groups:
                separated_groups.pop()
    
    return separated_groups