def is_bored(S):
    """
    Counts the number of boredoms in a given string.
    A boredom is a sentence starting with the word "I". Sentences are delimited by '.', '?' or '!'.
    
    Parameters:
    S (str): The input string to analyze.
    
    Returns:
    int: The number of boredoms in the string.
    """
    # Split the string into sentences using '.', '?', or '!'
    sentences = S.split('.')
    sentences.extend(S.split('?'))
    sentences.extend(S.split('!'))
    
    # Initialize the count of boredoms
    boredom_count = 0
    
    # Iterate over each sentence
    for sentence in sentences:
        # Strip leading whitespace and split by spaces
        words = sentence.strip().split()
        
        # Check if the first word is "I"
        if words[0] == "I":
            boredom_count += 1
    
    return boredom_count

# Example usage
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1