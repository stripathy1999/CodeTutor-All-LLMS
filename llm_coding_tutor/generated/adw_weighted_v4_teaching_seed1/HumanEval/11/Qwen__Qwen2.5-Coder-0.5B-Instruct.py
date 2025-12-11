def string_xor(a: str, b: str) -> str:
    """Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of binary XOR on the two input strings.
    """
    xor_result = ""
    for char_a, char_b in zip(a, b):
        if char_a!= char_b:
            xor_result += "1"
        else:
            xor_result += "0"
    return xor_result