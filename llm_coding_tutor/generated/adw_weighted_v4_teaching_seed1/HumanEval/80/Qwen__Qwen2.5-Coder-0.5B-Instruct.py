import re

def is_happy(s):
    """
    You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # Check if the string is shorter than 3 characters
    if len(s) < 3:
        return False
    
    # Check each substring of length 3
    for i in range(len(s) - 2):
        if len(set(s[i:i+3]))!= 3:
            return False
    
    return True