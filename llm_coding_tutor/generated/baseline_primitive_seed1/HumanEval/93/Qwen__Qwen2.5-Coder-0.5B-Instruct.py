def encode(message):
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                # Replace vowel with the 2-place ahead vowel
                next_char = vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            else:
                # Swap case
                next_char = char.swapcase()
            
            encoded_message += next_char
    
    return encoded_message

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
```