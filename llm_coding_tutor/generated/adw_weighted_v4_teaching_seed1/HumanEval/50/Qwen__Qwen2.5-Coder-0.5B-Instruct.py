import re
from collections import deque

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    # Create a deque to keep track of characters to be processed
    char_queue = deque(cleaned_string)
    
    # Initialize an empty list to store the encoded characters
    encoded_chars = []
    
    while char_queue:
        current_char = char_queue.popleft()
        
        # Calculate the new character by shifting it 5 positions forward
        shifted_char = chr(((ord(current_char) + 5 - ord("a")) % 26) + ord("a"))
        
        # Append the shifted character to the result list
        encoded_chars.append(shifted_char)
    
    # Join the list into a string and return it
    return "".join(encoded_chars)

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    # Create a deque to keep track of characters to be processed
    char_queue = deque(cleaned_string)
    
    # Initialize an empty list to store the decoded characters
    decoded_chars = []
    
    while char_queue:
        current_char = char_queue.popleft()
        
        # Calculate the new character by shifting it 5 positions backward
        shifted_char = chr(((ord(current_char) - 5 + ord("a")) % 26) + ord("a"))
        
        # Append the shifted character to the result list
        decoded_chars.append(shifted_char)
    
    # Join the list into a string and return it
    return "".join(decoded_chars)