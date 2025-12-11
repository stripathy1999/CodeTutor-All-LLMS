```python
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = "aeiouAEIOU"
    encoded_message = ""
    
    for char in message:
        if char.isalpha():
            # Swap case
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
            
            # Replace vowels with the next vowel in the alphabet
            if char in vowels:
                next_vowel = vowels[(vowels.index(char) + 2) % len(vowels)]
                encoded_message += next_vowel
            else:
                encoded_message += char
    
    return encoded_message

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output