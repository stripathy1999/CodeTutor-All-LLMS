```python
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # Define the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Rotate the alphabet by 2 positions
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    
    # Encrypt the input string
    encrypted_string = ""
    for char in s:
        if char in alphabet:
            # Find the index of the character in the rotated alphabet
            index = (alphabet.index(char) + 2) % len(rotated_alphabet)
            # Append the corresponding character from the rotated alphabet
            encrypted_string += rotated_alphabet[index]
        else:
            # If the character is not in the alphabet, append it unchanged
            encrypted_string += char
    
    return encrypted_string

# Test cases
print(