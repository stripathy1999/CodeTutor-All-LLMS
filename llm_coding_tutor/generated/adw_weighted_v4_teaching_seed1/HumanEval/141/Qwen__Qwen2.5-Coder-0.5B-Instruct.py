def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'.
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Split the file name by the dot
    parts = file_name.split('.')
    
    # Check if there are exactly two parts
    if len(parts)!= 2:
        return 'No'
    
    # Extract the first part
    first_part = parts[0]
    
    # Check if there are only three digits in the first part
    if not all(c.isdigit() for c in first_part):
        return 'No'
    
    # Extract the second part
    second_part = parts[1]
    
    # Check if the second part is one of the allowed file extensions
    allowed_extensions = ['txt', 'exe', 'dll']
    if second_part not in allowed_extensions:
        return 'No'
    
    return 'Yes'