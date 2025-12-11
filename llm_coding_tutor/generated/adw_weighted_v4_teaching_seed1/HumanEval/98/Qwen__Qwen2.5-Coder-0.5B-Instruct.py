def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Define the set of uppercase vowels
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}
    
    # Initialize a counter for uppercase vowels found at even indices
    upper_count = 0
    
    # Iterate over the string, checking only even indices
    for index in range(0, len(s), 2):
        if s[index] in uppercase_vowels:
            upper_count += 1
    
    return upper_count