from collections import Counter

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lowercase to ensure case insensitivity
    string = string.lower()
    
    # Use Counter to count occurrences of each character
    char_count = Counter(string)
    
    # Return the number of distinct characters
    return len(char_count)