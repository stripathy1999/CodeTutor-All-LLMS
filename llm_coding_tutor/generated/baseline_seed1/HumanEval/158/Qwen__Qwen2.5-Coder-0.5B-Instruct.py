from typing import List

def find_max(words: List[str]) -> str:
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""
    """
    # Initialize variables to store the maximum word and its unique character count
    max_word = ""
    max_unique_chars = 0
    
    # Iterate through each word in the list
    for word in words:
        # Count the number of unique characters in the current word
        unique_chars = len(set(word))
        
        # Check if this word has more unique characters or is lexicographically smaller
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < max_word):
            max_word = word
            max_unique_chars = unique_chars
    
    return max_word