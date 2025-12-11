def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups based on spaces
    groups = paren_string.split()
    
    # Initialize a list to store the maximum depth for each group
    max_depths = []
    
    # Iterate over each group
    for group in groups:
        current_depth = 0
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group