import re

def is_bored(S):
    # Split the sentence into sentences using regex to match '.', '?', or '!'
    sentences = re.split(r'[.!?]', S)
    
    # Initialize a counter for boredom
    boredom_count = 0
    
    # Iterate over each sentence
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            boredom_count += 1
    
    return boredom_count

# Test cases
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
```

This function uses regular expressions to split the input string into sentences and then iterates through each sentence to check if it starts with "I". If it does, it increments the `boredom_count`. Finally, it returns the total count of boredom.