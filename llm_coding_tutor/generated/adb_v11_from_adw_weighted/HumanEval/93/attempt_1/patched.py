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
            if char in vowels:
                # Find the next vowel in the alphabet
                next_vowel = vowels[(vowels.index(char) + 1) % len(vowels)]
                encoded_message += next_vowel
            else:
                # Swap case
                encoded_message += char.swapcase()
        else:
            # Non-alphabetic characters remain unchanged
            encoded_message += char
    
    return encoded_message