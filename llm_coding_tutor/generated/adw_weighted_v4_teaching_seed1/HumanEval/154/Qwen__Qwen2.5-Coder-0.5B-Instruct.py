def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Check if either word is empty
    if not a or not b:
        return False
    
    # Concatenate the first word with itself
    doubled_a = a + a
    
    # Check if b is a substring of doubled_a
    return b in doubled_a
# NOTE: Rubric corruption applied, dropped 3 hints
