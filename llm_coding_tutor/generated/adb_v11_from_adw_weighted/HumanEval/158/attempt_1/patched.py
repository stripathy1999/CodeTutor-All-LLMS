from collections import Counter

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""
    """
    # Count the number of unique characters in each word
    unique_chars = [len(set(word)) for word in words]
    
    # Find the word with the maximum number of unique characters
    max_unique_chars_index = unique_chars.index(max(unique_chars))
    
    # Return the word with the maximum number of unique characters
    return words[max_unique_chars_index]