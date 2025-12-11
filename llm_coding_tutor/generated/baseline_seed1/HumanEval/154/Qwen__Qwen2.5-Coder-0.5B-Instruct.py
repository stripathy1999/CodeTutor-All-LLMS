def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Check if the length of the second word is greater than the length of the first word
    if len(b) > len(a):
        return False
    
    # Concatenate the second word with itself
    doubled_b = b + b
    
    # Check if the second word is a substring of the concatenated word
    return b in doubled_b