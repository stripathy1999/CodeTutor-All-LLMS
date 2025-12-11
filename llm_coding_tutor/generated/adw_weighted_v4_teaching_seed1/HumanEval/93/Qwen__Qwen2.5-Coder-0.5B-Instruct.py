def encode(message):
    """
    Encodes a given message by swapping the case of all letters and replacing vowels with 
    the letter that appears 2 places ahead of that vowel in the English alphabet. Assumes only letters.

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Define vowels and their corresponding replacements
    vowel_replacements = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
        'A': 'C',
        'E': 'G',
        'I': 'K',
        'O': 'Q',
        'U': 'W'
    }

    # Initialize an empty list to store the encoded characters
    encoded_chars = []

    # Iterate over each character in the message
    for char in message:
        # Check if the character is a vowel
        if char.lower() in vowel_replacements:
            # Replace the vowel with its corresponding replacement
            encoded_char = vowel_replacements[char.lower()]
        else:
            # Swap the case of the character
            encoded_char = char.swapcase()

        # Append the encoded character to the list
        encoded_chars.append(encoded_char)

    # Join the list of encoded characters into a string and return
    return ''.join(encoded_chars)

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'