def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Check if the input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Initialize the sum of ASCII values of uppercase characters
    total_sum = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add its ASCII value to the total sum
            total_sum += ord(char)

    # Return the total sum
    return total_sum