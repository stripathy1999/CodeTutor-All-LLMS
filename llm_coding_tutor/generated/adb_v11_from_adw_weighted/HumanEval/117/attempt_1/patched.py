from typing import List

def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    if not s:
        return []

    # Split the string into words
    words = s.split()

    # Initialize a list to store words with exactly n consonants
    result = []

    # Iterate over each word
    for word in words:
        # Count the number of consonants in the word
        consonant_count = sum(1 for char in word if char.isalpha() and char not in 'aeiouAEIOU')

        # Check if the word has exactly n consonants
        if consonant_count == n:
            result.append(word)

    return result