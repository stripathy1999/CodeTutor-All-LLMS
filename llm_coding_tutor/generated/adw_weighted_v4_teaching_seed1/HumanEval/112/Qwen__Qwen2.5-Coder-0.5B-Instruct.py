def reverse_delete(s, c):
    # Check if both inputs are strings
    if not isinstance(s, str) or not isinstance(c, str):
        raise TypeError("Both inputs must be strings.")
    
    # Create a set of characters from the second string to avoid duplicates
    c_set = set(c)
    
    # Initialize an empty list to store characters to be deleted
    delete_chars = []
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is not in the set of characters to delete
        if char not in c_set:
            delete_chars.append(char)
    
    # Join the list of characters to form the result string
    result = ''.join(delete_chars)
    
    # Check if the result string is a palindrome
    return (result, result == result[::-1])