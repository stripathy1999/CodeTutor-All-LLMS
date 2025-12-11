# Function to find the list with total characters less than another list
def total_match(lst1, lst2):
    # Check if either list is empty
    if not lst1 or not lst2:
        return lst1  # Return the first list if both are empty
    
    # Calculate the total number of characters in all strings in the first list
    total_chars_lst1 = sum(len(s) for s in lst1)
    
    # Calculate the total number of characters in all strings in the second list
    total_chars_lst2 = sum(len(s) for s in lst2)
    
    # Compare the total characters of the two lists
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2

# Example usage
print(total_match([], []))  # Output: []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # Output: ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # Output: ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # Output: ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # Output: ['4']